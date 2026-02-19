from app.service.database import db
from app.models.user import User
from app.models.problem import Problem
from app.models.contest import Contest

def create_contest(name,description,start_time,end_time,creator_id):

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
    user = User.query.get(user_id)

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