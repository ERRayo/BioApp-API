from bioapi import ma
from marshmallow import fields

#Esquema de la tabla materias
class MateriaEsquema(ma.Schema):      
    id = fields.Integer()
    id_carrera = fields.Integer()
    nombre = fields.String()    
    
    #Esquemas que se mostraran con el equema de materia
    carrera = fields.Nested("CarreraEsquema")

#instancia de una sola materia
materia_esquema = MateriaEsquema()
#instancia de varias materia
materias_esquema = MateriaEsquema(many=True)
