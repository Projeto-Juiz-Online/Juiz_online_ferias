from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.service.submission_service import create_submission, list_submissions_by_problem, list_submissions_by_user

submission_bp = Blueprint('submission',__name__)

@submission_bp.route('/problems/<int:problem_id>/submission/new', methods=['GET','POST'])
def create_submission_controller(problem_id):

    if request.method == "POST":

        code = request.form.get("code")
        language = request.form.get("language")

        user_id = session.get("user_id")

        if not user_id:
            flash("Você precisa estar logado para enviar uma submissão.", "danger")
            return redirect(url_for("auth.login"))

        if not code or not language:

            flash("Por favor, preencha todos os campos.", "danger")
            return render_template("create_submission.html", problem_id=problem_id)
        
        try:
            create_submission(language,user_id,problem_id,code)
        except ValueError as e:
            flash(str(e), "danger")
            return redirect(url_for("problem.get_problem_controller", id=problem_id))
        
        flash("Submissão criada com sucesso!", "success")
        return redirect(url_for("problem.get_problem_controller", id=problem_id))

    return render_template("create_submission.html", problem_id=problem_id)

@submission_bp.route('/user/submissions')
def list_submission_by_user_controller():
    
    user_id = session.get("user_id")

    if not user_id:
        flash("Você precisa estar logado para ver suas submissões.", "danger")
        return redirect(url_for("auth.login"))
        
    submissions = list_submissions_by_user(user_id)

    submissions_by_problem = {}

    for sub in submissions:

        problem_id = sub.problem_id

        if problem_id not in submissions_by_problem:
            submissions_by_problem[problem_id] = {"problem": sub.problem,"submissions": []}

        submissions_by_problem[problem_id]["submissions"].append(sub)

    return render_template("list_user_submissions.html", submissions_by_problem=submissions_by_problem)

@submission_bp.route('/problems/<int:problem_id>/submissions')
def list_submission_by_problem_controller(problem_id):

    user_id = session.get("user_id")

    if not user_id:
        flash("Você precisa estar logado para ver as submissões.", "danger")
        return redirect(url_for("auth.login"))
    
    submissions = list_submissions_by_problem(problem_id)

    if not submissions:

        flash("Envie submissões primeiro para poder visualizá-las.")
        return redirect(url_for("submission.create_submission_controller",problem_id=problem_id))

    return render_template("list_problem_submissions.html",submissions=submissions,problem_id=problem_id)
