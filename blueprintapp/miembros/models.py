from blueprintapp import db

class Miembro(db.Model):
    __tablename__ = "miembros"
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    #rol = db.Column(db.String, nullable=True, default='')  # ← AGREGAR CAMPO rol
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"<MIEMBRO: {self.nombre} - {self.email}>"