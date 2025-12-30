from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.service.auth_service import create_user, check_password

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # verifica se os campos estão preenchidos / tripla verificação (front, back e db)
        if not username or not password or not username.strip() or not password.strip():
            flash('Por favor, preencha todos os campos.', 'danger')
            return render_template('register.html', username=username)

        # verifica se as senhas conferem
        if password != confirm_password:
            flash('As senhas não conferem.', 'danger')
            return render_template('register.html', username=username)
        else:
            user = create_user(username,password)

            if user: 
                flash(f'Usuário {username} criado com sucesso!', 'success')
                return redirect(url_for('auth.login'))
            else:
                flash('Erro ao criar conta. Esse nome de usuário já existe.', 'danger')
                return render_template('register.html')

    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        user = check_password(username,password)

        if user:
            session['user_id'] = user.id   
            session['username'] = user.username
            flash(f'Bem-vindo, {user.username}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Usuário ou senha incorretos.', 'danger')

    return render_template('login.html')
    
@auth_bp.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_id', None)
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('auth.login'))