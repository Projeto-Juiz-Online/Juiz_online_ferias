from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.service.contest_service import create_contest, add_user, add_problem, delete_contest, remove_user, remove_problem, list_contests, get_contest, get_contest_ranking
from datetime import datetime
from zoneinfo import ZoneInfo
from flask_login import login_required,  current_user
from app.utils.decorators import admin_required
from app.service.database import db
from app.models.contest import Contest
from app.models.submission import Submission  

contest_bp = Blueprint('contest',__name__)


def get_brazil_now_naive():
    return datetime.now(ZoneInfo("America/Sao_Paulo")).replace(tzinfo=None)

@contest_bp.route('/contests', methods=["GET"])
def list_contests_controller():

    contests = list_contests()
    now = get_brazil_now_naive()
    return render_template("list_contests.html", contests=contests, now=now)

@contest_bp.route('/contests/<int:id>', methods=['GET'])
def get_contest_controller(id):

    contest = get_contest(id)

    if not contest:
        flash("Contest não encontrado.", "danger")
        return redirect(url_for("contest.list_contests_controller"))

    now = get_brazil_now_naive()
    ranking = get_contest_ranking(id)
    return render_template("contest_detail.html", contest=contest, now=now, ranking=ranking)

@contest_bp.route('/contest/new', methods=['GET','POST'])
@login_required 
@admin_required
def create_contest_controller():

    if request.method == "POST":

        name = request.form.get("name")
        description = request.form.get("description")
        start_raw = request.form.get("start_time")
        end_raw = request.form.get("end_time")
        creator_id = int(request.form.get("creator_id"))

        if not name or not start_raw or not end_raw or not creator_id:

            flash("Por favor, preencha todos os campos.", "danger")
            return render_template("create_contest.html")

        try:
            br_tz = ZoneInfo("America/Sao_Paulo")
            start_time = datetime.fromisoformat(start_raw).replace(tzinfo=br_tz).replace(tzinfo=None)
            end_time = datetime.fromisoformat(end_raw).replace(tzinfo=br_tz).replace(tzinfo=None)
            
            create_contest(name, description, start_time, end_time, creator_id)
        except ValueError as e:
            flash(str(e), "danger")
            return redirect(url_for("contest.list_contests_controller"))
        
        flash("Contest Criado Com Sucesso!", "success")
        return redirect(url_for("contest.list_contests_controller"))

    return render_template("create_contest.html")

@contest_bp.route('/contest/new/user', methods=['GET','POST'])
@login_required 
@admin_required
def add_user_controller():

    if request.method=="POST":

        user_raw = request.form.get("user_id")
        contest_raw = request.form.get("contest_id")

        if not user_raw or not contest_raw:
            flash("Por favor, preencha todos os campos.", "danger")
            return render_template("add_user.html")

        contest_id = None
        try:
            user_id = int(user_raw)
            contest_id = int(contest_raw)
            add_user(user_id,contest_id)
        except ValueError as e:
            flash(str(e), "danger")
            if contest_id is not None:
                return redirect(url_for("contest.get_contest_controller", id=contest_id))
            return redirect(url_for("contest.add_user_controller"))

        flash("Usuario Adicionado Com Sucesso!", "success")
        return redirect(url_for("contest.get_contest_controller", id=contest_id))

    return render_template("add_user.html")

@contest_bp.route('/contest/new/problem', methods=['GET','POST'])
@login_required 
@admin_required
def add_problem_controller():

    if request.method=="POST":

        problem_raw = request.form.get("problem_id")
        contest_raw = request.form.get("contest_id")

        if not problem_raw or not contest_raw:
            flash("Por favor, preencha todos os campos.", "danger")
            return render_template("add_problem.html")

        try:
            problem_id = int(problem_raw)
            contest_id = int(contest_raw)
            add_problem(problem_id,contest_id)
        except ValueError as e:
            flash(str(e), "danger")
            return redirect(url_for("contest.add_problem_controller"))

        flash("Problema Adicionado Com Sucesso!", "success")
        return redirect(url_for("contest.list_contests_controller"))

    return render_template("add_problem.html")


#Apagar a contest e mantem as submissões.
@contest_bp.route('/delete/<int:contest_id>', methods=['POST'])
@login_required
@admin_required
def delete_contest_controller(contest_id):
    contest = Contest.query.get_or_404(contest_id)
    
    try:
        
        db.session.delete(contest)
        db.session.commit()
        
        flash(f'Contest "{contest.name}" removido com sucesso!', 'success')
        
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao deletar contest: {str(e)}', 'danger')
        print(f"Erro Delete Contest: {e}")
        
    return redirect(url_for('contest.list_contests_controller'))