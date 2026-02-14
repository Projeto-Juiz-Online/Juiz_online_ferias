from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.utils.decorators import admin_required
from app.service.database import db
from app.models.user import User
from app.models.problem import Problem
from app.models.submission import Submission
from sqlalchemy import desc

# Importando os Models
from app.models.test_case import TestCase 

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')
@login_required
@admin_required
def dashboard():
    total_users = User.query.count()
    total_problems = Problem.query.count()
    total_submissions = Submission.query.count()   
    recent_submissions = Submission.query.order_by(desc(Submission.id)).limit(5).all()

    return render_template(
        "admin_dashboard.html",
        total_users=total_users,
        total_problems=total_problems,
        total_submissions=total_submissions,
        recent_submissions=recent_submissions
    )

@admin_bp.route('/problems/new', methods=['GET', 'POST'])
@login_required
@admin_required
def new_problem():
    
    if request.method == 'POST':

        name = request.form.get('name')
        description = request.form.get('description')
        input_desc = request.form.get('input_description')
        output_desc = request.form.get('output_description')
        constraints = request.form.get('constraints')
        difficulty = request.form.get('difficulty')

        example_input = request.form.get('example_input')
        example_output = request.form.get('example_output')

        input_data = request.form.get('input_data')
        expected_output = request.form.get('expected_output')

        try:
            new_prob = Problem(
                name=name,
                description=description,
                input_description=input_desc,
                output_description=output_desc,
                constraints=constraints,
                difficulty=difficulty,
                example_input=example_input,
                example_output=example_output
            )

            db.session.add(new_prob)
            
            db.session.flush() 


            test_case = TestCase(
                problem_id=new_prob.id,
                input=input_data,               
                expected_output=expected_output
            )

            db.session.add(test_case)
            
            db.session.commit()

            flash(f'Problema "{name}" criado com sucesso!', 'success')
            return redirect(url_for('problem.list_problems_controller'))

        except Exception as e:
            db.session.rollback()
            print(f"Erro ao criar problema: {e}")
            flash(f'Erro ao criar problema. Verifique o terminal para detalhes.', 'danger')
            return render_template('create_problem.html')

    return render_template('create_problem.html')