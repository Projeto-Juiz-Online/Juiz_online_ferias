from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.service.test_case_service import create_test_case, list_test_cases
from app.service.problem_service import get_problem
from flask_login import login_required
from app.utils.decorators import admin_required

test_case_bp = Blueprint('test_case',__name__)

@test_case_bp.route('/problems/<int:problem_id>/testcases/new', methods=['GET','POST'])
@login_required
@admin_required
def create_test_case_controller(problem_id):
    
    problem = get_problem(problem_id)

    if not problem:
        flash("Problema não encontrado.", "danger")
        return redirect(url_for("problem.list_problems_controller"))
    
    if request.method == "POST":
        input_data = request.form.get("input_data")
        expected_output = request.form.get("expected_output")

        if not input_data or not expected_output:
            flash("Por favor, preencha todos os campos.", "danger")
            return render_template("create_test_case.html", problem=problem)
        
        try:
            create_test_case(problem_id, input_data, expected_output)
            flash("Caso de teste adicionado com sucesso!", "success") 
        except ValueError as e:
            flash(str(e), "danger")
            return redirect(url_for("problem.get_problem_controller", id=problem_id))

        return redirect(url_for("test_case.list_test_cases_controller", problem_id=problem_id))

    return render_template("create_test_case.html", problem=problem)


@test_case_bp.route("/problems/<int:problem_id>/testcases", methods=["GET"])
@login_required  
@admin_required  
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