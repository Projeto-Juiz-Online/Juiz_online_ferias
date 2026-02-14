from app import db

contest_problems = db.Table('contest_problems',
    db.Column('contest_id', db.Integer, db.ForeignKey('contests.id'), primary_key=True),
    db.Column('problem_id', db.Integer, db.ForeignKey('problems.id'), primary_key=True)
)

class Contest(db.Model):

    __tablename__ = "contests"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    problems = db.relationship("Problem", secondary=contest_problems, backref="contests")