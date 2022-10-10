from bioapi import ma
from marshmallow import fields

#Esquema de la tabla grupos
class GrupoEsquema(ma.Schema):     
    id = fields.Integer()
    id_profesor = fields.Integer()
    id_materia = fields.Integer()
    id_periodo = fields.Integer()
    aula = fields.String()
    grupo_estado = fields.Boolean()

    #Esquemas que se mostraran con el equema de grupo
    materia = fields.Nested("MateriaEsquema")
    profesor = fields.Nested("ProfesorEsquema")
    periodo = fields.Nested("PeriodoEsquema")
    horario = fields.Nested("HorarioEsquema", many=True)

#instancia de un solo grupo
grupo_esquema = GrupoEsquema()
#instancia de varios grupos
grupos_esquema = GrupoEsquema(many=True)