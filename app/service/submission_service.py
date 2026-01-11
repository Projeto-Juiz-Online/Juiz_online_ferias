from app import db
from app.models.submission import Submission
from app.models.problem import Problem
from app.models.user import User
from app.service.judge import judge
from app.service.runner.python_runner import run_python
from app.service.runner.c_runner import run_c
from app.service.runner.cpp_runner import run_cpp
from app.models.test_case import TestCase

# Tabela de Pontos Fixa
POINTS_TABLE = {
    "Iniciante": 10,
    "Fácil": 30,
    "Médio": 50,
    "Difícil": 100,
    "Lendário": 200
}

def create_submission(language,user_id,problem_id,code):

    problem = Problem.query.get(problem_id)
    if not problem:
        raise ValueError("Problema não existe")
    
    submission = Submission(status = "RUNNING", language = language, user_id = user_id, problem_id = problem_id, code = code)

    db.session.add(submission)
    db.session.commit()

    test_cases = TestCase.query.filter_by(problem_id=problem_id).all()
    
    total = len(test_cases)
    passed = 0
    failed = 0

    for test in test_cases:
        
        if language == "python":

            run_result = run_python(code,test.input)
            result = judge(run_result, test.expected_output)

        elif language == "c":

            run_result = run_c(code,test.input)
            result = judge(run_result, test.expected_output)

        elif language == "cpp":

            run_result = run_cpp(code,test.input)
            result = judge(run_result, test.expected_output)

        else:
            raise ValueError(f"Linguagem não suportada: {language}")

        if result["verdict"] != "AC":
            if result["verdict"] == "TLE" or result["verdict"] == "RUNTIME_ERROR": 
                submission.status = result["verdict"]
                submission.stdout = result["stdout"]
                submission.stderr = result["stderr"]
                submission.total_tests = total
                submission.passed_tests = passed
                submission.failed_tests = failed + 1
                db.session.commit()
                return submission
            else:
                failed += 1
                continue
        else:
            passed += 1

    if failed > 0:
        submission.status = "WA"
    else:
        submission.status = "AC"

    #Lógica de pontuação

    # Verifica se o usuário já havia resolvido o problema antes
    already_solved = Submission.query.filter(
        Submission.user_id == user_id,
        Submission.problem_id == problem_id,
        Submission.status == 'AC',
        Submission.id != submission.id
    ).count() 

    if already_solved == 0:
        user = User.query.get(user_id)
        # Busca a dificuldade do problema, caso não exista, define como "Iniciante" para evitar erros
        difficulty = getattr(problem, 'difficulty', 'Iniciante')
        points_to_add = POINTS_TABLE.get(difficulty, 10)  # Padrão para "Iniciante" se dificuldade não for encontrada

        #Garante que user.points não seja None e evita erros ao somar
        if user.points is None:
            user.points = 0

        user.points += points_to_add
        print(f"Adicionando {points_to_add} pontos ao usuário {user.username} por resolver o problema {problem.name}")

    submission.total_tests = total
    submission.passed_tests = passed
    submission.failed_tests = failed    
    submission.stdout = run_result["stdout"]
    submission.stderr = run_result["stderr"]
    
    db.session.commit()
    return submission

def list_submissions_by_user(user_id):

    return Submission.query.filter_by(user_id=user_id).all()

def list_submissions_by_problem(problem_id, user_id = None):

    query = Submission.query.filter_by(problem_id=problem_id)

    if user_id is not None:

        query = query.filter_by(user_id=user_id)

    return query.order_by(Submission.submitted_at.desc()).all()
