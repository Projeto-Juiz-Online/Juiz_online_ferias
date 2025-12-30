from app.service.database import db
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(username, password):

    user_exists = User.query.filter_by(username = username).first()
    if user_exists:
        return None
    
    hash = generate_password_hash(password)
    points = 0
    user = User(username = username, password_hash = hash, points = points)
    db.session.add(user)
    db.session.commit()
    return user

def check_password(username,password):

    user = User.query.filter_by(username = username).first()

    if not user:

        return None

    if check_password_hash(user.password_hash, password):
        return user
    
    return None
