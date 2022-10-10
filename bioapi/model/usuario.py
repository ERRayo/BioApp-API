from bioapi import db

#definicion del model de la tabla usuario
class usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    contraseña = db.Column(db.Text(), nullable=False)
    tipo_usuario = db.Column(db.String(50))
    #relaciones
    rprefecto = db.relationship('prefecto', backref=db.backref('usuario', lazy=True))

    def __init__(self,email,contraseña,tipo_usuario):
        self.email = email
        self.contraseña = contraseña
        self.tipo_usuario = tipo_usuario