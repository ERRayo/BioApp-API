from flask import request, jsonify, Blueprint
from sqlalchemy.orm import session 
from bioapi.schemas.carrera import carrera_esquema, carreras_esquema
from bioapi.model.carrera import carrera
from bioapi import db
from flask_jwt_extended import jwt_required
from flasgger import swag_from

ruta_carrera = Blueprint('ruta-carrera', __name__)

###endponit - GET all carreras 
@ruta_carrera.route('/carrera', methods=['GET'])
#@jwt_required()
@swag_from("../docs/carrera.yaml")
def get_carreras():
    all_carreras = carrera.query.all()
    result = carreras_esquema.dump(all_carreras)
    return jsonify(result)

###endpoint - GET from ID carrera
@ruta_carrera.route('/carrera/<id>', methods=['GET'])
def get_carrera(id):
    carrera_id = carrera.query.get(id)
    result = carrera_esquema.dump(carrera_id)
    return jsonify(result)

###endpoint - POST Creacion de carrera
@ruta_carrera.route('/carrera', methods=['POST'])
def create_carrera():
    nombre = request.json['nombre']
    plan_estudios = request.json['plan_estudios']
    new_carrera = carrera(nombre, plan_estudios)
    db.session.add(new_carrera)
    db.session.commit()
    result = carrera_esquema.dump(new_carrera)
    return jsonify(result)

###endpoint - PUT carrera
@ruta_carrera.route('/carrera/<id>', methods=['PUT'])
def update_carrera(id):
    carrera_update = carrera.query.get(id)
    nombre = request.json['nombre']
    plan_estudios = request.json['plan_estudios']
    carrera_update.nombre = nombre
    carrera_update.plan_estudios = plan_estudios
    db.session.commit()
    result = carrera_esquema.dump(carrera_update)
    return jsonify(result)

###endpoint - DELETE carrera
@ruta_carrera.route('/carrera/<id>', methods=['DELETE'])
def delete_carrera(id):
    carrera_delete = carrera.query.get(id)
    db.session.delete(carrera_delete)
    db.session.commit()
    result = carrera_esquema.dump(carrera_delete)
    return jsonify(result)