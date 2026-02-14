from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.service.contest import create_contest, add_user, add_problem, delete_contest, remove_user, remove_problem, list_contests
from datetime import datetime
from flask_login import login_required
from app.utils.decorators import admin_required

contest_bp = Blueprint('contest',__name__)

@contest_bp.route('/contests', methods=["GET"])
def list_contests_controller():

    contests = list_contests()
    return render_template("list_contests.html", contests = contests)

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
            start_time = datetime.fromisoformat(start_raw)
            end_time = datetime.fromisoformat(end_raw)
            create_contest(name, description, start_time, end_time, creator_id)
        except ValueError as e:
            flash(str(e), "danger")
            return redirect(url_for("contest.list_contests_controller"))
        
        flash("Contest Criado Com Sucesso!", "success")
        return redirect(url_for("contest.list_contests_controller"))

    return render_template("create_contest.html")