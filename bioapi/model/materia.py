from bioapi import db

#definicion del model de la tabla materia
class materia(db.Model):
    __tablename__ = 'materia'
    id = db.Column(db.Integer, primary_key=True)  
    id_carrera = db.Column(db.Integer, db.ForeignKey('carrera.id'))
    nombre = db.Column(db.String(50))  
    #Relaciones
    rgrupoa = db.relationship('grupo', backref=db.backref('materia', lazy=True))   

    def __init__(self,id_carrera, nombre):
        self.id_carrera = id_carrera
        self.nombre = nombre