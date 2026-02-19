from app import db
from sqlalchemy.ext.associationproxy import association_proxy

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    points = db.Column(db.Integer, nullable=True)
    
    is_admin = db.Column(db.Boolean, default=False)
    contest_registrations = db.relationship("ContestRegistration", back_populates="user", cascade="all, delete-orphan")
    contests_joined = association_proxy("contest_registrations", "contest")
    

    def __repr__(self):
        return f"<User {self.username}>"
    

    # o Flask-Login exige ter 4 métodos especificos, sao eles: is_authenticated, is_active, is_anonymous, get_id
    @property
    def is_authenticated(self):
        """
        Retorna True se o usuário forneceu credenciais válidas.
        """
        return True 
    
    @property
    def is_active(self):
        """
        Retorna True se a conta estiver ativa.
        """
        return True

    @property
    def is_anonymous(self):
        """
        Retorna False, pois usuários reais (logados) nunca são anônimos
        """
        return False
    
    def get_id(self):
        """
        O Flask-Login precisa de um ID único em formato de TEXTO (String).
        É por isso que converti self.id para string aqui.
        """
        return str(self.id)