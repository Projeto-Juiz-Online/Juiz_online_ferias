from app import db

class Problem(db.Model):
    
    __tablename__ = "problems"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    input_description = db.Column(db.Text, nullable=False)
    output_description = db.Column(db.Text, nullable=False)
    constraints = db.Column(db.Text, nullable = False)

    def __repr__(self):
        return f"<Problem {self.name}>"