from bioapi import ma
from marshmallow import fields

#Esquema de la tabla usuario
class UsuarioEsquema(ma.Schema):
    id = fields.Integer()
    email = fields.String()
    tipo_usuario = fields.String()

#instancia de una sola asistencia de alumno
usuario_esquema = UsuarioEsquema()
#instancia de varias asistencias de alumnos
usuarios_esquema = UsuarioEsquema(many=True)