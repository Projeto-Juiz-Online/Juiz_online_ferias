from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.service.contest import create_contest, add_user, add_problem, delete_contest, remove_user, remove_problem, list_contests

contest_bp = Blueprint('contest',__name__)

@contest_bp.route("/contests", methods=["GET"])
def list_contests_controller():

    contests = list_contests()
    return render_template("list_contests.html", contests = contests)

