from app.models.user import User
from sqlalchemy import desc

def get_ranking():
    return User.query.order_by(desc(User.points)).all()