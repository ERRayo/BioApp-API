from bioapi.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT
from unittest import result
from flask import Flask, request, jsonify, Blueprint 
from bioapi.schemas.profesor import profesores_esquema, profesor_esquema
from bioapi.model.profesor import profesor
from bioapi.model.huella_profesor import huella_profesor
from bioapi.schemas.huella_profesor import huella_esquema, huellas_esquema
from bioapi import db

ruta_profesor = Blueprint('ruta-profesor', __name__)

###endponit - GET all profesores 
@ruta_profesor.route('/profesor', methods=['GET'])
def get_profesores():
    all_profesores = profesor.query.all()
    result = profesores_esquema.dump(all_profesores)
    return jsonify(result)

###endpoint - GET from ID profesor
@ruta_profesor.route('/profesor/<id>', methods=['GET'])
def get_profesor(id):
    profesor_id = profesor.query.get(id)
    result = profesor_esquema.dump(profesor_id)
    return jsonify(result)

###endpoint - POST Creacion de profesor
@ruta_profesor.route('/profesor', methods=['POST'])
def create_profesor():
    nombre = request.json['nombre']
    apellido_paterno = request.json['apellido_paterno']
    apellido_materno = request.json['apellido_materno']
    no_trabajador = request.json['no_trabajador']
    new_profesor = profesor(nombre, apellido_paterno, apellido_materno, no_trabajador)
    db.session.add(new_profesor)
    db.session.commit()
    result = profesor_esquema.dump(new_profesor)
    return jsonify(result)

###endpoint - POST Crearcio de profesor con huella (Primero profesor despues huella)
@ruta_profesor.route('/profesor/huella', methods=['POST'])
def create_profesorHuella():
    nombre = request.json['nombre']
    apellido_paterno = request.json['apellido_paterno']
    apellido_materno = request.json['apellido_materno']
    no_trabajador = request.json['no_trabajador']
    ##Datos de huella
    huella_principal = request.json['huella_principal']
    huella_secundaria = request.json['huella_secundaria']

    new_profesor = profesor(nombre, apellido_paterno, apellido_materno, no_trabajador)
    db.session.add(new_profesor)
    db.session.commit()
    db.session.refresh(new_profesor)
    new_huella = huella_profesor(new_profesor.id, huella_principal, huella_secundaria)
    db.session.add(new_huella)
    db.session.commit()

    result = huella_esquema.dump(new_huella)
    return jsonify(result), HTTP_201_CREATED


###endpoint - PUT profesor
@ruta_profesor.route('/profesor/<id>', methods=['PUT'])
def update_profesor(id):
    profesor_update = profesor.query.get(id)
    nombre = request.json['nombre']
    apellido_paterno = request.json['apellido_paterno']
    apellido_materno = request.json['apellido_materno']
    no_trabajador= request.json['no_trabajador']
    profesor_update.nombre = nombre
    profesor_update.apellido_paterno = apellido_paterno
    profesor_update.apellido_materno = apellido_materno
    profesor_update.no_trabajador = no_trabajador
    db.session.commit()
    result = profesor_esquema.dump(profesor_update)
    return jsonify(result)

###endpoint - DELETE profesor
@ruta_profesor.route('/profesor/<id>', methods=['DELETE'])
def delete_profesor(id):
    profesor_delete = profesor.query.get(id)
    result = profesor_esquema.dump(profesor_delete)
    db.session.delete(profesor_delete)
    db.session.commit()
    return jsonify(result)