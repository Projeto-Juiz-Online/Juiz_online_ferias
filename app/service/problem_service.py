from app.service.database import db
from app.models.problem import Problem

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

    db.session.delete(problem)
    db.session.commit()

    return problem