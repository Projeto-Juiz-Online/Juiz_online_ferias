from app import db

class Problem(db.Model):
    
    __tablename__ = "problems"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    input_description = db.Column(db.Text, nullable=False)
    output_description = db.Column(db.Text, nullable=False)
    constraints = db.Column(db.Text, nullable = False)
    test_cases = db.relationship("TestCase", backref="problem", cascade = "all, delete-orphan")
    submissions = db.relationship('Submission', backref='problem', lazy=True, cascade="all, delete-orphan")
    difficulty = db.Column(db.String(50), default="Iniciante", nullable=False)
    example_input = db.Column(db.Text, default="Entrada de exemplo não cadastrada", nullable=False)
    example_output = db.Column(db.Text, default="Saída de exemplo não cadastrada", nullable=False)

    def __repr__(self):
        return f"<Problem {self.name} - Difficulty: {self.difficulty}>"