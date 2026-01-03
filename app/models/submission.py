from app import db
from datetime import datetime, timezone

class Submission(db.Model):

    __tablename__ = "submissions"

    id = db.Column(db.Integer, primary_key = True)
    status = db.Column(db.String(30), nullable = False, default="PENDING")
    language = db.Column(db.String(30), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey('problems.id', ondelete='CASCADE'), nullable=False)
    submitted_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc)) #essa e a data da submissao
    code = db.Column(db.Text, nullable = False)    #esse e o codigo do problema
    user = db.relationship("User", backref="submissions") #essas duas ultimas linhas e so pra facilitar a escrever o codigo
    

