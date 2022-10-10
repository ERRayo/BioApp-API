from bioapi import ma
from marshmallow import fields

#Esquema de la tabla carreras
class CarreraEsquema(ma.Schema):
    id = fields.Integer()
    nombre = fields.String()
    plan_estudios = fields.String()    

#instancia de una sola carrera
carrera_esquema = CarreraEsquema()
#instancia de varias carreras
carreras_esquema = CarreraEsquema(many = True)
