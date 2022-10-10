from bioapi import db

#definicion del model de la tabla grupos
class grupo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_profesor = db.Column(db.Integer, db.ForeignKey('profesor.id'))
    id_materia = db.Column(db.Integer, db.ForeignKey('materia.id'))
    id_periodo = db.Column(db.Integer, db.ForeignKey('periodo.id'))
    aula = db.Column(db.String(50))
    grupo_estado = db.Column(db.Boolean)
    #Relaciones
    rasistencia = db.relationship('asistencia', backref=db.backref('grupo', lazy=True))
     
    def __init__(self, id_profesor, id_materia, id_periodo, aula, grupo_estado):
        self.id_profesor = id_profesor    
        self.id_materia = id_materia
        self.id_periodo = id_periodo
        self.aula = aula
        self.grupo_estado = grupo_estado