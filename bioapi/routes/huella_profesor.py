from flask import request, jsonify, Blueprint
from sqlalchemy.orm import session 
from bioapi.schemas.huella_profesor import huella_esquema, huellas_esquema
from bioapi.model.huella_profesor import huella_profesor
from bioapi import db

ruta_huella = Blueprint('ruta-huella', __name__)

###endponit - GET all alumnos 
@ruta_huella.route('/huella', methods=['GET'])
def get_huellas():
    all_huellas = huella_profesor.query.all()
    result = huellas_esquema.dump(all_huellas)
    return jsonify(result)

###endpoint - GET from ID alumno
@ruta_huella.route('/huella/<id>', methods=['GET'])
def get_huella(id):
    huella_id = huella_profesor.query.get(id)
    result = huella_esquema.dump(huella_id)
    return jsonify(result)

###endpoint - GET from ID alumno
@ruta_huella.route('/huella/profesor/<id_profesor>', methods=['GET'])
def get_huella_idprofesor(id_profesor):
    huella_id = db.session.query(huella_profesor).filter(huella_profesor.id_profesor == id_profesor).first()
    result = huella_esquema.dump(huella_id)
    return jsonify(result)

###endpoint - POST Creacion de alumno
@ruta_huella.route('/huella', methods=['POST'])
def create_huella():
    id_profesor = request.json['id_profesor']
    huella_principal = request.json['huella_principal']
    huella_secundaria = request.json['huella_secundaria']
    new_huella = huella_profesor(id_profesor, huella_principal, huella_secundaria)
    db.session.add(new_huella)
    db.session.commit()
    result = huella_esquema.dump(new_huella)
    return jsonify(result)

###endpoint - PUT alumno
@ruta_huella.route('/huella/<id>', methods=['PUT'])
def update_huella(id):
    huella_update = huella_profesor.query.get(id)
    id_profesor = request.json['id_profesor']
    huella_principal = request.json['huella_principal']
    huella_secundaria = request.json['huella_secundaria']
    huella_update.id_profesor = id_profesor
    huella_update.huella_principal = huella_principal
    huella_update.huella_secundaria = huella_secundaria
    db.session.commit()
    result = huella_esquema.dump(huella_update)
    return jsonify(result)

###endpoint - DELETE alumno
@ruta_huella.route('/huella/<id>', methods=['DELETE'])
def delete_huella(id):
    huella_delete = huella_profesor.query.get(id)
    result = huella_esquema.dump(huella_delete)
    db.session.delete(huella_delete)
    db.session.commit()
    return jsonify(result)