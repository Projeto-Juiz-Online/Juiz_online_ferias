from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.service.test_case_service import create_test_case, list_test_cases
from app.service.problem_service import get_problem

test_case_bp = Blueprint('test_case',__name__)

@test_case_bp.route('/problems/<int:problem_id>/testcases/new', methods=['GET','POST'])
def create_test_case_controller(problem_id):

    if request.method == "POST":

        input_data = request.form.get("input_data")
        expected_output = request.form.get("expected_output")

        if not input_data or not expected_output:

            flash("Por favor, preencha todos os campos.", "danger")
            return render_template("create_test_case.html", problem_id=problem_id)
        
        try:
            create_test_case(problem_id, input_data, expected_output)
        except ValueError as e:
            flash(str(e), "danger")
            return redirect(url_for("problem.get_problem_controller", id=problem_id))

        flash("Caso de teste criado com sucesso!", "success")
        return redirect(url_for("test_case.list_test_cases_controller", problem_id=problem_id))

    return render_template("create_test_case.html", problem_id = problem_id)



@test_case_bp.route("/problems/<int:problem_id>/testcases", methods=["GET"])
def list_test_cases_controller(problem_id):

    problem = get_problem(problem_id)
    if not problem:
        flash("Problema não encontrado.", "danger")
        return redirect(url_for("problem.list_problems_controller"))

    test_cases = list_test_cases(problem_id)

    return render_template(
        "list_test_cases.html",
        problem=problem,
        test_cases=test_cases
    )