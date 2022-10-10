from bioapi import ma
from marshmallow import fields

#Esquema de la tabla usuario
class HuellaEsquema(ma.Schema):
    id = fields.Integer()
    id_profesor = fields.Integer()
    huella_principal = fields.String()
    huella_secundaria = fields.String()
    #Esquemas que se mostraran con el equema de materia
    profesor = fields.Nested("ProfesorEsquema")

#instancia de una sola asistencia de alumno
huella_esquema = HuellaEsquema()
#instancia de varias asistencias de alumnos
huellas_esquema = HuellaEsquema(many=True)