from flask import Flask, render_template
import os
from app.service.database import db, migrate
from flask_login import LoginManager

from app.controller.auth_controller import auth_bp  # blueprint auth
from app.controller.problem_controller import problem_bp
from app.controller.test_case_controller import test_case_bp
from app.controller.submission_controller import submission_bp
from app.controller.ranking_controller import ranking_bp    
from app.controller.admin_controller import admin_bp
from app.controller.contest_controller import contest_bp    


def create_app():
    app = Flask(__name__)
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "database.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models import user, problem, submission

    login_manager = LoginManager()
    login_manager.init_app(app)

    login_manager.login_view= 'auth.login'
    login_manager.login_message = "Por favor, faça login para acessar essa página."
    login_manager.login_message_category = "info"

    from app.models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(auth_bp)
    app.register_blueprint(problem_bp)
    app.register_blueprint(test_case_bp)
    app.register_blueprint(submission_bp)
    app.register_blueprint(ranking_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(contest_bp)

    @app.route("/")
    def home():
        return render_template("home.html")

    return app
