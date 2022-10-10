from bioapi import db

#definicion del model de la tabla horario
class horario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_grupo = db.Column(db.Integer, db.ForeignKey('grupo.id'))
    lunes = db.Column(db.TIME) 
    lunes_fin = db.Column(db.TIME) 
    martes = db.Column(db.TIME) 
    martes_fin = db.Column(db.TIME) 
    miercoles = db.Column(db.TIME) 
    miercoles_fin = db.Column(db.TIME) 
    jueves = db.Column(db.TIME) 
    jueves_fin = db.Column(db.TIME) 
    viernes = db.Column(db.TIME) 
    viernes_fin = db.Column(db.TIME) 
    sabado = db.Column(db.TIME) 
    sabado_fin = db.Column(db.TIME) 

    #Relacion
    rgrupo = db.relationship('grupo', backref=db.backref('horario', lazy=True))

    def __init__(self, id_grupo, lunes, lunes_fin, martes, martes_fin, miercoles, miercoles_fin, jueves, jueves_fin, viernes, viernes_fin, sabado, sabado_fin):
        self.id_grupo = id_grupo
        self.lunes = lunes
        self.lunes_fin = lunes_fin
        self.martes = martes
        self.martes_fin = martes_fin
        self.miercoles = miercoles
        self.miercoles_fin = miercoles_fin
        self.jueves = jueves
        self.jueves_fin = jueves_fin
        self.viernes = viernes
        self.viernes_fin = viernes_fin
        self.sabado = sabado
        self.sabado_fin = sabado_fin