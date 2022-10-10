from bioapi import ma
from marshmallow import fields

#Esquema de la tabla profesores
class ProfesorEsquema(ma.Schema):    
    id = fields.Integer()
    nombre = fields.String()
    apellido_paterno = fields.String()
    apellido_materno = fields.String()
    no_trabajador = fields.String()
    #Esquemas que se mostraran con el equema de grupo
    grupo = fields.Nested("GrupoEsquema")
    

#instancia de un solo profesor
profesor_esquema = ProfesorEsquema()
#instancia de varios profesores
profesores_esquema = ProfesorEsquema(many=True)
