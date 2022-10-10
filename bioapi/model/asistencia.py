from bioapi import db

#definicion del model de la tabla asistencia
class asistencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    id_grupo = db.Column(db.Integer, db.ForeignKey('grupo.id'))
    id_prefecto = db.Column(db.Integer, db.ForeignKey('prefecto.id'))
    fecha = db.Column(db.DATE)  
    hora = db.Column(db.TIME) 
    asistencia_estado = db.Column(db.Boolean) 
    descripcion = db.Column(db.String(50))
    
    def __init__(self, id_grupo, id_prefecto, fecha, hora, asistencia_estado, descripcion,):
        self.id_grupo = id_grupo
        self.id_prefecto = id_prefecto
        self.fecha = fecha
        self.hora = hora
        self.asistencia_estado = asistencia_estado
        self.descripcion = descripcion
        