from bioapi import ma
from marshmallow import fields

#Esquema de la tabla horarios
class HorarioEsquema(ma.Schema):
    id = fields.Integer()
    id_grupo = fields.Integer()
    lunes = fields.Time()
    lunes_fin = fields.Time()
    martes = fields.Time()
    martes_fin = fields.Time() 
    miercoles = fields.Time()
    miercoles_fin = fields.Time()
    jueves = fields.Time()
    jueves_fin = fields.Time()
    viernes = fields.Time()
    viernes_fin = fields.Time()
    sabado = fields.Time()
    sabado_fin = fields.Time()  

#instancia de un solo horario
horario_esquema = HorarioEsquema()
#instancia de varios horarios
horarios_esquema = HorarioEsquema(many=True)