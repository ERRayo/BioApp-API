from bioapi import db

#definicion del model de la tabla huella_profesor
class huella_profesor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_profesor= db.Column(db.Integer, db.ForeignKey('profesor.id'))
    huella_principal = db.Column(db.String(512))
    huella_secundaria = db.Column(db.String(512))
    

    def __init__(self,id_profesor,huella_principal, huella_secundaria):
        self.id_profesor = id_profesor
        self.huella_principal = huella_principal
        self.huella_secundaria = huella_secundaria
