from flask import Flask, render_template
import os
from app.service.database import db, migrate
from app.controller.auth_controller import auth_bp  # blueprint auth
from app.controller.problem_controller import problem_bp
from app.controller.test_case_controller import test_case_bp
from app.controller.submission_controller import submission_bp

def create_app():
    app = Flask(__name__)
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "database.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models import user, problem, submission

    with app.app_context():
        db.create_all() 

    app.register_blueprint(auth_bp)
    app.register_blueprint(problem_bp)
    app.register_blueprint(test_case_bp)
    app.register_blueprint(submission_bp)

    @app.route("/")
    def home():
        return render_template("home.html")

    return app
