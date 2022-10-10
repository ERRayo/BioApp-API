from bioapi import ma
from marshmallow import fields

#Esquema de la tabla asistencias
class AsistenciaEsquema(ma.Schema):
    id = fields.Integer()
    id_grupo= fields.Integer()
    id_prefecto = fields.Integer()
    fecha= fields.Date()
    hora = fields.Time()
    asistencia_estado = fields.Boolean()
    descripcion = fields.String()
    #Esquemas que se mostraran con el equema de materia
    grupo = fields.Nested("GrupoEsquema")
    prefecto = fields.Nested("PrefectoEsquema")

#instancia de una sola asistencia
asistencia_esquema = AsistenciaEsquema()
#instancia de varias asistencias
asistencias_esquema = AsistenciaEsquema(many=True)
