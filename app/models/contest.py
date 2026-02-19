from app import db
from sqlalchemy.ext.associationproxy import association_proxy

contest_problems = db.Table('contest_problems',
    db.Column('contest_id',db.Integer,db.ForeignKey('contests.id'), primary_key=True),
    db.Column('problem_id',db.Integer,db.ForeignKey('problems.id'), primary_key=True)
)

class ContestRegistration(db.Model):

    __tablename__ = 'contest_registrations'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    contest_id = db.Column(db.Integer, db.ForeignKey('contests.id'), primary_key=True)
    points = db.Column(db.Integer, nullable=False, default=0)

    user = db.relationship("User", back_populates="contest_registrations")
    contest = db.relationship("Contest", back_populates="registrations")

class Contest(db.Model):

    __tablename__ = "contests"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    description = db.Column(db.Text,nullable=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    creator = db.relationship("User", foreign_keys=[creator_id], backref="created_contests")
    problems = db.relationship("Problem", secondary=contest_problems, backref="contests")
    registrations = db.relationship("ContestRegistration", back_populates="contest", cascade="all, delete-orphan")
    users = association_proxy("registrations", "user")
