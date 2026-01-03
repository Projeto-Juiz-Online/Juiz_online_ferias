from app.service.database import db
from app.models.problem import Problem
from app.models.submission import Submission

def create_problem(name, description, input_description, output_description, constraints):

    problem = Problem(name = name,description = description,input_description = input_description,output_description = output_description,constraints = constraints)

    db.session.add(problem)
    db.session.commit()
    return problem

def get_problem(id):

    problem = Problem.query.filter_by(id=id).first()

    if not problem:

        return None
    
    return problem

def search_problems_by_name(query):

    return Problem.query.filter(Problem.name.ilike(f"%{query}%")).all()

def list_problems():

    return Problem.query.all()

def delete_problem(id):

    problem = Problem.query.filter_by(id=id).first()

    if not problem:

        return None

    Submission.query.filter_by(problem_id=id).delete()
    db.session.delete(problem)
    db.session.commit()

    return problem