from flask import Flask, request, jsonify, Blueprint 
from bioapi.schemas.prefecto import prefectos_esquema, prefecto_esquema
from bioapi.model.prefecto import prefecto
from bioapi import db

ruta_prefecto = Blueprint('ruta-prefecto', __name__)

###endponit - GET all profesores 
@ruta_prefecto.route('/prefecto', methods=['GET'])
def get_prefectos():
    all_prefectos = prefecto.query.all()
    result = prefectos_esquema.dump(all_prefectos)
    return jsonify(result)

###endpoint - GET from ID profesor
@ruta_prefecto.route('/prefecto/<id>', methods=['GET'])
def get_prefecto(id):
    prefecto_id = prefecto.query.get(id)
    result = prefecto_esquema.dump(prefecto_id)
    return jsonify(result)

###endpoint - GET from ID profesor
@ruta_prefecto.route('/prefecto/user/<id>', methods=['GET'])
def get_prefecto_user(id):
    prefecto_id = prefecto.query.filter(prefecto.id_usuario == id).first()
    result = prefecto_esquema.dump(prefecto_id)
    return jsonify(result)

###endpoint - POST Creacion de profesor
@ruta_prefecto.route('/prefecto', methods=['POST'])
def create_prefecto():
    id_usuario = request.json['id_usuario']
    nombre = request.json['nombre']
    apellido_paterno = request.json['apellido_paterno']
    apellido_materno = request.json['apellido_materno']
    new_prefecto = prefecto(id_usuario, nombre, apellido_paterno, apellido_materno)
    db.session.add(new_prefecto)
    db.session.commit()
    result = prefecto_esquema.dump(new_prefecto)
    return jsonify(result)

###endpoint - PUT profesor
@ruta_prefecto.route('/prefecto/<id>', methods=['PUT'])
def update_prefector(id):
    prefecto_update = prefecto.query.get(id)
    id_usuario = request.json['id_usuario']
    nombre = request.json['nombre']
    apellido_paterno = request.json['apellido_paterno']
    apellido_materno = request.json['apellido_materno']
    prefecto_update.id_usuario = id_usuario
    prefecto_update.nombre = nombre
    prefecto_update.apellido_paterno = apellido_paterno
    prefecto_update.apellido_materno = apellido_materno

    db.session.commit()
    result = prefecto_esquema.dump(prefecto_update)
    return jsonify(result)

###endpoint - DELETE profesor
@ruta_prefecto.route('/prefecto/<id>', methods=['DELETE'])
def delete_prefecto(id):
    prefecto_delete = prefecto.query.get(id)
    result = prefecto_esquema.dump(prefecto_delete)
    db.session.delete(prefecto_delete)
    db.session.commit()
    return jsonify(result)