from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.service.problem_service import create_problem, list_problems, get_problem, search_problems_by_name

problem_bp = Blueprint('problem', __name__)

@problem_bp.route('/problems/new', methods = ['GET','POST'])
def create_problem_controller():

    if request.method == "POST":

        name = request.form.get("name")
        description = request.form.get("description")
        input_description = request.form.get("input_description")   
        output_description = request.form.get("output_description")
        constraints = request.form.get("constraints")

        if not name or not description or not input_description or not output_description or not constraints:

            flash("Por favor, preencha todos os campos.", "danger")
            return render_template("create_problem.html")
        
        problem = create_problem(name,description,input_description,output_description,constraints)
        
        flash("Problema criado com sucesso!", "success")
        return redirect(url_for("problem.get_problem", id=problem.id))

    return render_template("create_problem.html")


@problem_bp.route("/problems", methods=["GET"])
def list_problems_controller():

    query = request.args.get("search")

    if query:
        problems = search_problems_by_name(query)
    else:
        problems = list_problems()

    return render_template("list_problems.html", problems=problems)

@problem_bp.route("/problems/<int:id>", methods=["GET"])
def get_problem_controller(id):

    problem = get_problem(id)

    if not problem:
        flash("Problema não encontrado.", "danger")
        return redirect(url_for("problem.list_problems"))

    return render_template("problem_detail.html", problem=problem)

