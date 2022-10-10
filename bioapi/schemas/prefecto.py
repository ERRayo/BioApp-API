from bioapi import ma
from marshmallow import fields

#Esquema de la tabla prefecto
class PrefectoEsquema(ma.Schema):    
    id = fields.Integer()
    id_usuario = fields.Integer()
    nombre = fields.String()
    apellido_paterno = fields.String()
    apellido_materno = fields.String()
    #Esquemas que se mostraran con el equema de materia
    usuario = fields.Nested("UsuarioEsquema")


#instancia de un solo profesor
prefecto_esquema = PrefectoEsquema()
#instancia de varios profesores
prefectos_esquema = PrefectoEsquema(many=True)