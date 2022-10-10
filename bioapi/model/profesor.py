from bioapi import db

#definicion del model de la tabla profesor
class profesor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido_paterno = db.Column(db.String(50))
    apellido_materno = db.Column(db.String(50))
    no_trabajador = db.Column(db.String(50))
    #Relaciones
    #rgrupo = db.relationship('grupo', backref=db.backref('profesor', lazy=True))
    #Relaciones
    rhuella = db.relationship('huella_profesor', backref=db.backref('profesor', lazy=True))
    rprofesor = db.relationship('grupo', backref=db.backref('profesor', lazy=True))
    
    

    def __init__(self,nombre,apellido_paterno, apellido_materno,no_trabajador):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.no_trabajador = no_trabajador