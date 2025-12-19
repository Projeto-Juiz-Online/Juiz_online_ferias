from app import db
from app.models.test_case import TestCase
from app.models.problem import Problem

def create_test_case(problem_id,input_data,expected_output):

    problem = Problem.query.get(problem_id)
    if not problem:
        raise ValueError("Problema não existe")

    test_case = TestCase(problem_id=problem_id,input=input_data,expected_output=expected_output)

    db.session.add(test_case)
    db.session.commit()

    return test_case
