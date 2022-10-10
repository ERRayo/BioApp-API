from bioapi import ma
from marshmallow import fields

#Esquema de la tabla periodo
class PeriodoEsquema(ma.Schema):
    id = fields.Integer()
    fecha_ini = fields.Date()
    fecha_fin = fields.Date()

#instancia de una sola periodo
periodo_esquema = PeriodoEsquema()
#instancia de varias periodo
periodos_esquema = PeriodoEsquema(many=True)