from app import db

contest_problems = db.Table('contest_problems',
    db.Column('contest_id',db.Integer,db.ForeignKey('contests.id'), primary_key=True),
    db.Column('problem_id',db.Integer,db.ForeignKey('problems.id'), primary_key=True)
)

contest_registrations = db.Table('contest_registrations',
    db.Column('user_id',db.Integer,db.ForeignKey('users.id'), primary_key=True),
    db.Column('contest_id',db.Integer,db.ForeignKey('contests.id'), primary_key=True)
)

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
    users = db.relationship("User", secondary=contest_registrations, backref = "contests_joined")
