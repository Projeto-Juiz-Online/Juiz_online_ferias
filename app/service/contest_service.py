from app.service.database import db
from app.models.user import User
from app.models.problem import Problem
from app.models.contest import Contest
from datetime import datetime

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

    if user in contest.users:
        raise ValueError("Este usuário já está registrado neste contest.")

    contest.users.append(user)
    db.session.commit()
    return user

def remove_user(user_id, contest_id):

    contest = Contest.query.get(contest_id)
    user = User.query.get(user_id)

    contest.users.remove(user)
    db.session.commit()
    return user

def add_problem(problem_id, contest_id):

    contest = Contest.query.get(contest_id)
    problem = Problem.query.get(problem_id)

    contest.problems.append(problem)
    db.session.commit()
    return problem

def remove_problem(problem_id, contest_id):

    contest = Contest.query.get(contest_id)
    problem = Problem.query.get(problem_id)

    contest.problems.remove(problem)
    db.session.commit()
    return problem

def list_contests():
    return Contest.query.all()

def get_contest(contest_id):
    return Contest.query.get(contest_id)

def is_contest_possible(start_time, end_time) -> bool:

    if start_time <= datetime.now():
        return False
    
    if end_time <= start_time:
        return False

    return True

def is_contest_running(start_time, end_time) -> bool:

    if datetime.now() >= start_time and datetime.now()<=end_time:

        return True
    
    return False

