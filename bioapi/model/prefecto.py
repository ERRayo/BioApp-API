from bioapi import db

#definicion del model de la tabla prefecto
class prefecto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    nombre = db.Column(db.String(50))
    apellido_paterno = db.Column(db.String(50))
    apellido_materno = db.Column(db.String(50))
    #Relaciones
    rasistencia = db.relationship('asistencia', backref=db.backref('prefecto', lazy=True))
    

    def __init__(self, id_usuario, nombre, apellido_paterno, apellido_materno):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        