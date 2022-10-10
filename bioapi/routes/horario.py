from flask import request, jsonify, Blueprint
from sqlalchemy.orm import session
from bioapi.schemas.horario import horario_esquema, horarios_esquema
from bioapi.model.horario import horario
from bioapi import db

ruta_horario = Blueprint('ruta-horario', __name__)


###endponit - GET all horarios
@ruta_horario.route('/horario', methods=['GET'])
def get_horarios():
    all_horarios = horario.query.all()
    result = horarios_esquema.dump(all_horarios)
    return jsonify(result)

###endpoint - GET from ID horario
@ruta_horario.route('/horario/<id>', methods=['GET'])
def get_alumno(id):
    horario_id = horario.query.get(id)
    result = horario_esquema.dump(horario_id)
    return jsonify(result)

###endpoint - POST Creacion de horario
@ruta_horario.route('/horario', methods=['POST'])
def create_horario():
    id_grupo = request.json['id_grupo']
    
    lunes = request.json['lunes']
    lunes_fin = request.json['lunes_fin']
    martes = request.json['martes']
    martes_fin = request.json['martes_fin']
    miercoles = request.json['miercoles']
    miercoles_fin = request.json['miercoles_fin']
    jueves = request.json['jueves']
    jueves_fin = request.json['jueves_fin']
    viernes = request.json['viernes']
    viernes_fin = request.json['viernes_fin']
    sabado = request.json['sabado']
    sabado_fin = request.json['sabado_fin']

    new_horario = horario(id_grupo, lunes, lunes_fin, martes, martes_fin, miercoles, miercoles_fin, jueves, jueves_fin, viernes, viernes_fin, sabado, sabado_fin)
    db.session.add(new_horario)
    db.session.commit()
    result = horario_esquema.dump(new_horario)
    return jsonify(result)

###endpoint - PUT horario
@ruta_horario.route('/horario/<id>', methods=['PUT'])
def update_horario(id):
    horario_update = horario.query.get(id)
    id_grupo = request.json['id_grupo']
    lunes = request.json['lunes']
    lunes_fin = request.json['lunes_fin']
    martes = request.json['martes']
    martes_fin = request.json['martes_fin']
    miercoles = request.json['miercoles']
    miercoles_fin = request.json['miercoles_fin']
    jueves = request.json['jueves']
    jueves_fin = request.json['jueves_fin']
    viernes = request.json['viernes']
    viernes_fin = request.json['viernes_fin']
    sabado = request.json['sabado']
    sabado_fin = request.json['sabado_fin']

    horario_update.id_grupo = id_grupo
    horario_update.lunes = lunes
    horario_update.lunes_fin = lunes_fin
    horario_update.martes = martes
    horario_update.martes_fin = martes_fin
    horario_update.miercoles = miercoles
    horario_update.miercoles_fin = miercoles_fin
    horario_update.jueves = jueves
    horario_update.jueves_fin = jueves_fin
    horario_update.viernes = viernes
    horario_update.viernes_fin = viernes_fin
    horario_update.sabado = sabado
    horario_update.sabado_fin = sabado_fin

    db.session.commit()
    result = horario_esquema.dump(horario_update)
    return jsonify(result)

###endpoint - DELETE horario
@ruta_horario.route('/horario/<id>', methods=['DELETE'])
def delete_horario(id):
    horario_delete = horario.query.get(id)
    result = horario_esquema.dump(horario_delete)
    db.session.delete(horario_delete)
    db.session.commit()
    return jsonify(result)