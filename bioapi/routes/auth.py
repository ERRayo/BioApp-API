from bioapi.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT
from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
import validators
from bioapi.model.prefecto import prefecto
from bioapi.model.usuario import usuario
from bioapi.model.profesor import profesor
from bioapi.schemas.usuario import usuario_esquema, usuarios_esquema 
from bioapi.schemas.prefecto import prefectos_esquema, prefecto_esquema
from bioapi.schemas.profesor import profesor_esquema
from bioapi import db
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
from flasgger import swag_from
from flask_cors import cross_origin

auth = Blueprint('auth-user', __name__, url_prefix='/auth/user')

#@cross_origin
@auth.route('/register', methods=['POST'])
#@swag_from('./docs/register.yaml')
def register():
    email = request.json['email']
    contraseña = request.json['contraseña']
    tipo_usuario = request.json['tipo_usuario']

    if len(contraseña) < 6:
        return jsonify({'error': "Password is too short"}), HTTP_400_BAD_REQUEST

    if not validators.email(email):
        return jsonify({'error': "Email is not valid"}), HTTP_400_BAD_REQUEST

    if usuario.query.filter_by(email=email).first() is not None:
        return jsonify({'error': "Email is taken"}), HTTP_409_CONFLICT

    pwd_hash = generate_password_hash(contraseña)

    new_ausuario = usuario(email, pwd_hash, tipo_usuario)

    db.session.add(new_ausuario)
    db.session.commit()

    result = usuario_esquema.dump(new_ausuario)
    return jsonify(result), HTTP_201_CREATED

#@cross_origin
@auth.route('/login', methods=['POST'])
@swag_from("../docs/login.yaml")
def login():
    email = request.json.get('email','')
    password = request.json.get('password','')

    print('>>>>>>>>>>>>>>', email)
    print('>>>>>>>>>>>>>>', password)

    usuarios_login = usuario.query.filter_by(email=email).first()
    print('--------->>>>',usuarios_login)

    if usuarios_login:
        is_pass_correct = check_password_hash(usuarios_login.contraseña, password)
        print('----------------------->>>>',is_pass_correct)
        

        if is_pass_correct:
            refresh = create_refresh_token(identity = usuarios_login.id)
            access = create_access_token(identity = usuarios_login.id)

            return jsonify({
                'user': {
                    'refresh': refresh,
                    'access': access,
                    'email': usuarios_login.email,
                    'tipo_usuario': usuarios_login.tipo_usuario
                }

            }), HTTP_200_OK
    return jsonify({'error': 'Wrong credentials'}), HTTP_401_UNAUTHORIZED

#@cross_origin
@auth.route('/me', methods=['GET'])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    usuario_logueado = usuario.query.filter_by(id = user_id).first()

    result = usuario_esquema.dump(usuario_logueado)
    return jsonify(result), HTTP_200_OK


@auth.route('/token/refresh', methods=['GET'])
@jwt_required(refresh=True)
def refresh_users_token():
    identity = get_jwt_identity()
    access = create_access_token(identity=identity)

    return jsonify({
        'access': access
    }), 

#@cross_origin
@auth.route('/register/prefecto', methods=['POST'])
#@swag_from('./docs/register.yaml')
def registerPrefecto():
    email = request.json['email']
    contraseña = request.json['contraseña']
    tipo_usuario = request.json['tipo_usuario']
    nombre = request.json['nombre']
    apellido_paterno = request.json['apellido_paterno']
    apellido_materno = request.json['apellido_materno']


    if len(contraseña) < 6:
        return jsonify({'error': "Password is too short"}), HTTP_400_BAD_REQUEST

    if not validators.email(email):
        return jsonify({'error': "Email is not valid"}), HTTP_400_BAD_REQUEST

    if usuario.query.filter_by(email=email).first() is not None:
        return jsonify({'error': "Email is taken"}), HTTP_409_CONFLICT

    pwd_hash = generate_password_hash(contraseña)

    new_ausuario = usuario(email, pwd_hash, tipo_usuario)
    db.session.add(new_ausuario)
    db.session.commit()
    db.session.refresh(new_ausuario)
    new_prefecto = prefecto(new_ausuario.id, nombre, apellido_paterno, apellido_materno)
    db.session.add(new_prefecto)
    db.session.commit()

    result = profesor_esquema.dump(new_prefecto)
    return jsonify(result), HTTP_201_CREATED


@auth.route('/update/prefecto/<id>', methods=['PUT'])
#@swag_from('./docs/register.yaml')
def updatePrefecto(id):
    prefecto_update = prefecto.query.get(id)
    id_usuario = request.json['id_usuario']
    nombre = request.json['nombre']
    apellido_paterno = request.json['apellido_paterno']
    apellido_materno = request.json['apellido_materno']
    
    prefecto_update.id_usuario = id_usuario
    prefecto_update.nombre = nombre
    prefecto_update.apellido_paterno = apellido_paterno
    prefecto_update.apellido_materno = apellido_materno

    usuario_update = db.session.query(usuario).filter(usuario.id == id_usuario).first()
    
    email = request.json['email']
    contraseña = request.json['contraseña']

    if len(contraseña) < 6:
        return jsonify({'error': "Password is too short"}), HTTP_400_BAD_REQUEST

    if not validators.email(email):
        return jsonify({'error': "Email is not valid"}), HTTP_400_BAD_REQUEST

    pwd_hash = generate_password_hash(contraseña)

    usuario_update.email = email
    usuario_update.contraseña = pwd_hash
    usuario_update.tipo_usuario = 'Prefecto'
   

    db.session.commit()
    result = prefecto_esquema.dump(prefecto_update)
    return jsonify(result), HTTP_200_OK