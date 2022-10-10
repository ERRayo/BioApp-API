from bioapi import db

#definicion del model de la tabla carrera
class carrera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    plan_estudios = db.Column(db.String(50))
    #Relaciones
    rmateria= db.relationship('materia', backref=db.backref('carrera', lazy=True), foreign_keys='materia.id_carrera')

    def __init__(self,nombre,plan_estudios):
        self.nombre = nombre
        self.plan_estudios = plan_estudios