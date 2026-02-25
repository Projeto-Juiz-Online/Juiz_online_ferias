from app.service.database import db
from app.models.user import User
from app.models.problem import Problem
from app.models.contest import Contest, ContestRegistration
from datetime import datetime
from zoneinfo import ZoneInfo


def get_brazil_now_naive():
    return datetime.now(ZoneInfo("America/Sao_Paulo")).replace(tzinfo=None)

def create_contest(name,description,start_time,end_time,creator_id):

    if not is_contest_possible(start_time, end_time):
        if end_time <= start_time:
            raise ValueError("O horário de término deve ser maior que o horário de início.")
        raise ValueError("O horário de início deve ser no futuro.")

    contest = Contest(name=name, description=description, start_time=start_time, end_time=end_time, creator_id=creator_id)

    db.session.add(contest)
    db.session.commit()
    return contest

def delete_contest(contest_id):

    contest = Contest.query.get(contest_id)
    db.session.delete(contest)
    db.session.commit()
    return contest

def add_user(user_id, contest_id):

    contest = Contest.query.get(contest_id)

    if not contest:
        raise ValueError("Contest não encontrado.")

    if not is_contest_running(contest.start_time, contest.end_time):
        raise ValueError("O contest não está aberto para inscrições. Verifique os horários de início e fim.")

    user = User.query.get(user_id)

    if not user:
        raise ValueError("Usuário não encontrado.")

    existing_registration = ContestRegistration.query.filter_by(user_id=user_id, contest_id=contest_id).first()
    if existing_registration:
        raise ValueError("Este usuário já está registrado neste contest.")

    registration = ContestRegistration(user_id=user_id, contest_id=contest_id, points=0)
    db.session.add(registration)
    db.session.commit()
    return user

def remove_user(user_id, contest_id):

    registration = ContestRegistration.query.filter_by(user_id=user_id, contest_id=contest_id).first()
    if not registration:
        raise ValueError("Inscrição não encontrada para este usuário neste contest.")

    user = registration.user
    db.session.delete(registration)
    db.session.commit()
    return user

def add_problem(problem_id, contest_id):

    contest = Contest.query.get(contest_id)
    problem = Problem.query.get(problem_id)

    if not contest:
        raise ValueError("Contest não encontrado.")

    if not problem:
        raise ValueError("Problema não encontrado.")

    if not problem.belongs_only_to_contest:
        raise ValueError("Problema pertence ao treino livre.")

    if problem in contest.problems:
        raise ValueError("Problema já adicionado neste contest.")

    contest.problems.append(problem)
    db.session.commit()
    return problem

def remove_problem(problem_id, contest_id):

    contest = Contest.query.get(contest_id)
    problem = Problem.query.get(problem_id)

    if not contest:
        raise ValueError("Contest não encontrado.")

    if not problem:
        raise ValueError("Problema não encontrado.")

    if problem not in contest.problems:
        raise ValueError("Problema não está neste contest.")

    contest.problems.remove(problem)
    db.session.commit()
    return problem

def list_contests():
    return Contest.query.all()

def get_contest(contest_id):
    return Contest.query.get(contest_id)

def get_contest_ranking(contest_id):
    return ContestRegistration.query.filter_by(contest_id=contest_id).join(User).order_by(
        ContestRegistration.points.desc(),
        User.username.asc()
    ).all()

def is_contest_possible(start_time, end_time) -> bool:

    if start_time <= get_brazil_now_naive():
        return False
    
    if end_time <= start_time:
        return False

    return True

def is_contest_running(start_time, end_time) -> bool:

    now = get_brazil_now_naive()
    if now >= start_time and now <= end_time:

        return True
    
    return False

