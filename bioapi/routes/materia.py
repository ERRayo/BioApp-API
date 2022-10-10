from flask import request, jsonify, Blueprint
from sqlalchemy.orm import session 
from bioapi.schemas.materia import materia_esquema, materias_esquema
from bioapi.model.materia import materia
from bioapi.model.profesor import profesor
from bioapi import db

ruta_materia = Blueprint('ruta-materia', __name__)

###endponit - GET all materias 
@ruta_materia.route('/materia', methods=['GET'])
def get_materias(): 
    all_materias = materia.query.all()
    result = materias_esquema.dump(all_materias)
    return jsonify(result)

###endpoint - GET from ID materia
@ruta_materia.route('/materia/<id>', methods=['GET'])
def get_materia(id):
    materia_id = db.session.query(materia).get(id)
    result = materia_esquema.dump(materia_id)
    return jsonify(result)

###endpoint - GET from ID carrera
@ruta_materia.route('/materia/carrera/<id>', methods=['GET'])
def get_materiacarrera(id):
    materia_id = db.session.query(materia).filter(materia.id_carrera == id).all()
    result = materias_esquema.dump(materia_id)
    return jsonify(result)

###endpoint - POST Creacion de materia
@ruta_materia.route('/materia', methods=['POST'])
def create_materia():
    id_carrera = request.json['id_carrera']
    nombre = request.json['nombre'] 
    new_materia = materia(id_carrera, nombre)
    db.session.add(new_materia)
    db.session.commit()
    result = materia_esquema.dump(new_materia)
    return jsonify(result)

###endpoint - PUT materia
@ruta_materia.route('/materia/<id>', methods=['PUT'])
def update_meteria(id):
    materia_update = materia.query.get(id)
    id_carrera = request.json['id_carrera']
    nombre = request.json['nombre'] 
    materia_update.id_carrera = id_carrera
    materia_update.nombre = nombre  
    db.session.commit()
    result = materia_esquema.dump(materia_update)
    return jsonify(result)

###endpoint - DELETE materia
@ruta_materia.route('/materia/<id>', methods=['DELETE'])
def delete_materia(id):
    materia_delete = materia.query.get(id)
    result = materia_esquema.dump(materia_delete)
    db.session.delete(materia_delete)
    db.session.commit()
    return jsonify(result)