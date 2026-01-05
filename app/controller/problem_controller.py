from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.service.problem_service import create_problem, list_problems, get_problem, search_problems_by_name, delete_problem
from app.service.test_case_service import create_test_case
from app.service.submission_service import list_submissions_by_problem
from flask_login import login_required, current_user
from app.utils.decorators import admin_required

problem_bp = Blueprint('problem', __name__)

# --- NOTA: A rota de CRIAR PROBLEMA foi removida daqui ---
# Ela agora está  no admin_controller.py para ficar mais organizado.
# ---------------------------------------------------------

@problem_bp.route("/problems", methods=["GET"])
def list_problems_controller():

    query = request.args.get("search")

    if query:
        problems = search_problems_by_name(query)
    else:
        problems = list_problems()

    return render_template("list_problems.html", problems=problems)

@problem_bp.route("/problems/<int:id>/delete", methods=["POST"])
@login_required  
@admin_required  
def delete_problem_controller(id):

    try:
        delete_problem(id)
        flash("Problema deletado com sucesso!", "success")
    except Exception as e:
        flash(f"Erro ao deletar: {e}", "danger")
        
    return redirect(url_for('problem.list_problems_controller'))

    

@problem_bp.route("/problems/<int:id>", methods=["GET"])
def get_problem_controller(id):
    problem = get_problem(id)

    if not problem:
        flash("Problema não encontrado.", "danger")
        return redirect(url_for("problem.list_problems_controller"))
    
    user_submissions = []
    
    if current_user.is_authenticated:
        user_submissions = list_submissions_by_problem(problem_id=id, user_id=current_user.id)

    return render_template("problem_detail.html", problem=problem, submissions=user_submissions)