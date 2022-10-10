from bioapi import db

#definicion del model de la tabla periodo
class periodo(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    fecha_ini = db.Column(db.Date)  
    fecha_fin = db.Column(db.Date)  
    #Relaciones
    rgrupo = db.relationship('grupo', backref=db.backref('periodo', lazy=True))
    
    def __init__(self,fecha_ini,fecha_fin):
        self.fecha_ini = fecha_ini
        self.fecha_fin = fecha_fin