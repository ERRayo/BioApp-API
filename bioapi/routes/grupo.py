from flask import request, jsonify, Blueprint
from sqlalchemy.orm import session
from bioapi.model.profesor import profesor
from bioapi.schemas.grupo import grupo_esquema, grupos_esquema
from bioapi.model.grupo import grupo
from bioapi.model.horario import horario
from bioapi import db
from sqlalchemy import func, case

ruta_grupo = Blueprint('ruta-grupo', __name__)

###endponit - GET all grupos 
@ruta_grupo.route('/grupo', methods=['GET'])
def get_grupos():
    all_grupos = grupo.query.all()
    result = grupos_esquema.dump(all_grupos)
    return jsonify(result)

###endpoint - GET from ID grupo
@ruta_grupo.route('/grupo/<id>', methods=['GET'])
def get_grupo(id):
    grupo_id = grupo.query.get(id)
    result = grupo_esquema.dump(grupo_id)
    return jsonify(result)

###endpoint - GET from ID grupo
@ruta_grupo.route('/grupo/profesor/<id>/<id_periodo>', methods=['GET'])
def get_grupo_profesor(id, id_periodo):
    grupo_id = grupo.query.join(profesor, grupo.id_profesor == profesor.id).filter(grupo.id_profesor == id).filter(grupo.id_periodo == id_periodo)
    print('>>>>>>>>>>>>>>', grupo_id)
    result = grupos_esquema.dump(grupo_id)
    return jsonify(result)

###endpoint - GET from ID grupo --------------------------------------------------------------------------
@ruta_grupo.route('/grupo/profesor/fecha/<id>/<id_periodo>', methods=['GET'])
def get_grupo_profesor_fecha(id, id_periodo):
      
    xpr = case(
        [
            (func.dayofweek(func.current_date()) == 2, (func.current_timestamp() >= horario.lunes) & (func.current_timestamp() <= horario.lunes_fin)),
            (func.dayofweek(func.current_date()) == 3, (func.current_timestamp() >= horario.martes) & (func.current_timestamp() <= horario.martes_fin)),
            (func.dayofweek(func.current_date()) == 4, (func.current_timestamp() >= horario.miercoles) & (func.current_timestamp() <= horario.miercoles_fin)),
            (func.dayofweek(func.current_date()) == 5, (func.current_timestamp() >= horario.jueves) & (func.current_timestamp() <= horario.jueves_fin)),
            (func.dayofweek(func.current_date()) == 6, (func.current_timestamp() >= horario.viernes) & (func.current_timestamp() <= horario.viernes_fin)),
            (func.dayofweek(func.current_date()) == 7, (func.current_timestamp() >= horario.sabado) & (func.current_timestamp() <= horario.sabado_fin))
        ]
    )
    grupo_id = db.session.query(grupo).join(horario, grupo.id == horario.id_grupo).filter(xpr).filter(grupo.id_profesor == id).filter(grupo.id_periodo == id_periodo).first()
    print('>>>>>>>>>>>>>>', grupo_id)
    result = grupo_esquema.dump(grupo_id)
    return jsonify(result)

###endpoint - POST Creacion de grupo
@ruta_grupo.route('/grupo', methods=['POST'])
def create_grupo():
    id_profesor = request.json['id_profesor']
    id_materia = request.json['id_materia']
    id_periodo = request.json['id_periodo']
    aula = request.json['aula']
    grupo_estado = request.json['grupo_estado']
    new_grupo = grupo(id_profesor, id_materia, id_periodo, aula, grupo_estado)
    db.session.add(new_grupo)
    db.session.commit()
    result = grupo_esquema.dump(new_grupo)
    return jsonify(result)

###endpoint - POST Creacion de grupo
@ruta_grupo.route('/grupo/horario', methods=['POST'])
def create_grupo_horario():
    id_profesor = request.json['id_profesor']
    id_materia = request.json['id_materia']  
    id_periodo = request.json['id_periodo']
    aula = request.json['aula']
    grupo_estado = request.json['grupo_estado'] 
    
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

    new_grupo = grupo(id_profesor, id_materia, id_periodo, aula, grupo_estado)
    db.session.add(new_grupo)
    db.session.commit()
    db.session.refresh(new_grupo)

    new_horario = horario(new_grupo.id, lunes, lunes_fin, martes, martes_fin, miercoles, miercoles_fin, jueves, jueves_fin, viernes, viernes_fin, sabado, sabado_fin)
    db.session.add(new_horario)
    db.session.commit()

    result = grupo_esquema.dump(new_grupo)
    return jsonify(result)

###endpoint - PUT grupo y horario
@ruta_grupo.route('/grupo/horario/<id>', methods=['PUT'])
def update_grupoHorario(id):
    grupo_update = grupo.query.get(id)

    id_profesor = request.json['id_profesor']
    id_materia = request.json['id_materia']
    id_periodo = request.json['id_periodo']
    aula = request.json['aula']
    grupo_estado = request.json['grupo_estado']

    grupo_update.id_profesor = id_profesor
    grupo_update.id_materia = id_materia
    grupo_update.id_periodo = id_periodo
    grupo_update.aula = aula
    grupo_update.grupo_estado = grupo_estado

    horario_update = db.session.query(horario).filter(horario.id_grupo == id).first()

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
    result = grupo_esquema.dump(grupo_update)
    return jsonify(result)

###endpoint - PUT grupo
@ruta_grupo.route('/grupo/<id>', methods=['PUT'])
def update_grupo(id):
    grupo_update = grupo.query.get(id)
    id_profesor = request.json['id_profesor']
    id_materia = request.json['id_materia']
    id_periodo = request.json['id_periodo']
    aula = request.json['aula']
    grupo_estado = request.json['grupo_estado']

    grupo_update.id_profesor = id_profesor
    grupo_update.id_materia = id_materia
    grupo_update.id_periodo = id_periodo
    grupo_update.aula = aula
    grupo_update.grupo_estado = grupo_estado
    
    db.session.commit()
    result = grupo_esquema.dump(grupo_update)
    return jsonify(result)

###endpoint - DELETE grupo
@ruta_grupo.route('/grupo/<id>', methods=['DELETE'])
def delete_grupo(id):
    grupo_delete = grupo.query.get(id)
    result =grupo_esquema.dump(grupo_delete)
    db.session.delete(grupo_delete)
    db.session.commit()
    return jsonify(result)