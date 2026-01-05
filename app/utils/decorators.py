from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Verifica se o usuário está logado E se é admin
        if not current_user.is_authenticated or not current_user.is_admin:
            flash("Acesso negado. Área restrita a administradores.", "danger")
            # Se não for admin, manda de volta para a Home
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function