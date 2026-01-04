from app import db
from app.models.submission import Submission
from app.models.problem import Problem
from app.models.user import User

def create_submission(language,user_id,problem_id,code):

    problem = Problem.query.get(problem_id)
    if not problem:
        raise ValueError("Problema não existe")
    
    submission = Submission(status = "PENDING", language = language, user_id = user_id, problem_id = problem_id, code = code)

    db.session.add(submission)
    db.session.commit()

    return submission

def list_submissions_by_user(user_id):

    return Submission.query.filter_by(user_id=user_id).all()

def list_submissions_by_problem(problem_id, user_id = None):

    query = Submission.query.filter_by(problem_id=problem_id)

    if user_id is not None:

        query = query.filter_by(user_id=user_id)

    return query.order_by(Submission.submitted_at.desc()).all()
