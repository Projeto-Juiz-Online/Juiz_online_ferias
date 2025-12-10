from flask import Flask

app = Flask(__name__)

# Rota de teste
@app.route("/")
def home():
    return "Servidor rodando! 🚀"

# Importando controllers
from app.controller import auth_controller, problem_controller, submission_controller