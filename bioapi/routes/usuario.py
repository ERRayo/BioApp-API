from flask import request, jsonify, Blueprint
from sqlalchemy.orm import session 
from bioapi.schemas.usuario import usuario_esquema, usuarios_esquema
from bioapi.model.usuario import usuario
from bioapi import db

ruta_usuario = Blueprint('ruta-usuario', __name__)

###endponit - GET all alumnos 
@ruta_usuario.route('/usuario', methods=['GET'])
def get_usuarios():
    all_usuarios = usuario.query.all()
    result = usuarios_esquema.dump(all_usuarios)
    return jsonify(result)

###endpoint - GET from ID alumno
@ruta_usuario.route('/usuario/<id>', methods=['GET'])
def get_usuario(id):
    usuario_id = usuario.query.get(id)
    result = usuario_esquema.dump(usuario_id)
    return jsonify(result)

###endpoint - POST Creacion de alumno
@ruta_usuario.route('/usuario', methods=['POST'])
def create_usuario():
    email = request.json['email']
    contraseña = request.json['contraseña']
    tipo_usuario = request.json['tipo_usuario']
    new_ausuario = usuario(email, contraseña, tipo_usuario)
    db.session.add(new_ausuario)
    db.session.commit()
    result = usuario_esquema.dump(new_ausuario)
    return jsonify(result)

###endpoint - PUT alumno
@ruta_usuario.route('/usuario/<id>', methods=['PUT'])
def update_usuario(id):
    usuario_update = usuario.query.get(id)
    email = request.json['email']
    contraseña = request.json['contraseña']
    tipo_usuario = request.json['tipo_usuario']
    usuario_update.email = email
    usuario_update.contraseña = contraseña
    usuario_update.tipo_usuario = tipo_usuario
    db.session.commit()
    result = usuario_esquema.dump(usuario_update)
    return jsonify(result)

###endpoint - DELETE alumno
@ruta_usuario.route('/usuario/<id>', methods=['DELETE'])
def delete_usuarioo(id):
    usuario_delete = usuario.query.get(id)
    result = usuario_esquema.dump(usuario_delete)
    db.session.delete(usuario_delete)
    db.session.commit()
    return jsonify(result)