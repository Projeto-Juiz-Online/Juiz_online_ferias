from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.service.problem_service import create_problem, list_problems, get_problem, search_problems_by_name, delete_problem
from app.service.test_case_service import create_test_case
from app.service.submission_service import list_submissions_by_problem
from flask_login import login_required, current_user
from app.utils.decorators import admin_required
from app.models.problem import Problem

problem_bp = Blueprint('problem', __name__)

# --- NOTA: A rota de CRIAR PROBLEMA foi removida daqui ---
# Ela agora está  no admin_controller.py para ficar mais organizado.
# ---------------------------------------------------------

@problem_bp.route("/problems", methods=["GET"])
def list_problems_controller():
    search = request.args.get("search")
    difficulty = request.args.get("difficulty")

    query = Problem.query.filter_by(belongs_only_to_contest=False)

    if search:
        query = query.filter(Problem.name.ilike(f"%{search}%"))
    
    if difficulty and difficulty != 'Todos':
        query = query.filter_by(difficulty=difficulty)

    problems = query.all()

    return render_template("list_problems.html", problems=problems, current_diff=difficulty)

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

    if problem.belongs_only_to_contest and (not current_user.is_authenticated or not current_user.is_admin):
        flash("Este problema é exclusivo de torneio.", "danger")
        return redirect(url_for("problem.list_problems_controller"))
    
    user_submissions = []
    
    if current_user.is_authenticated:
        user_submissions = list_submissions_by_problem(problem_id=id, user_id=current_user.id)

    return render_template("problem_detail.html", problem=problem, submissions=user_submissions)