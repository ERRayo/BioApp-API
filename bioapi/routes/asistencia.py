from flask import request, jsonify, Blueprint
from sqlalchemy import func, null
from sqlalchemy.orm import session 
from bioapi.schemas.asistencia import asistencia_esquema, asistencias_esquema
from bioapi.model.asistencia import asistencia
from bioapi.model.grupo import grupo
from bioapi import db

ruta_asistencia = Blueprint('ruta-asistencia', __name__)

###endponit - GET all asistencias 
@ruta_asistencia.route('/asistencia', methods=['GET'])
def get_asistencias():
    all_asistencia = asistencia.query.all()
    result = asistencias_esquema.dump(all_asistencia)
    return jsonify(result)

###endpoint - GET from ID asistencia
@ruta_asistencia.route('/asistencia/<id>', methods=['GET'])
def get_asistencia(id):
    asistencia_id = asistencia.query.get(id)
    result = asistencia_esquema.dump(asistencia_id)
    return jsonify(result)

###endpoint - POST Creacion de asistencia
@ruta_asistencia.route('/asistencia', methods=['POST'])
def create_asistencia():
    id_grupo = request.json['id_grupo']
    id_prefecto = request.json['id_prefecto']
    asistencia_estado = request.json['asistencia_estado']
    descripcion = request.json['descripcion']

    new_asistencia = asistencia(id_grupo, id_prefecto, func.current_date(), func.current_timestamp(), asistencia_estado, descripcion)
    db.session.add(new_asistencia)
    db.session.commit()
    result = asistencia_esquema.dump(new_asistencia)
    return jsonify(result)

###endpoint - PUT alumno
@ruta_asistencia.route('/asistencia/<id>', methods=['PUT'])
def update_asistencia(id):
    asistencia_update = asistencia.query.get(id)
    id_grupo = request.json['id_grupo']
    id_prefecto = request.json['id_prefecto']
    fecha = request.json['fecha']
    hora = request.json['hora']
    asistencia_estado = request.json['asistencia_estado']
    descripcion = request.json['descripcion']

    asistencia_update.id_grupo = id_grupo
    asistencia_update.id_prefecto = id_prefecto
    asistencia_update.fecha = fecha
    asistencia_update.hora = hora
    asistencia_update.asistencia_estado = asistencia_estado
    asistencia_update.descripcion = descripcion

    db.session.commit()
    result = asistencia_esquema.dump(asistencia_update)
    return jsonify(result)

###endpoint - DELETE asistencia
@ruta_asistencia.route('/asistencia/<id>', methods=['DELETE'])
def delete_asistencia(id):
    asistencia_delete = asistencia.query.get(id)
    result = asistencia_esquema.dump(asistencia_delete)
    db.session.delete(asistencia_delete)
    db.session.commit()
    return jsonify(result)


###endpoint - POST Creacion de asistencia
@ruta_asistencia.route('/asistencia/reporte', methods=['POST'])
def reporte_asistencia():
    id_profesor = request.json['id_profesor']
    id_periodo = request.json['id_periodo']
    fecha_ini = request.json['fecha_ini']
    fecha_fin = request.json['fecha_fin']
    print('----------------------->>>> Profesor: ', id_profesor)
    print('----------------------->>>> Periodo: ', id_periodo)
    print('----------------------->>>> Fecha ini: ', fecha_ini)
    print('----------------------->>>> Fecha fin: ', fecha_fin)

    reporte = db.session.query(asistencia).all()
    print('------------>>>>>>>>>normal:', reporte)

    ## Periodo
    if id_periodo != '' and id_profesor == '' and fecha_ini == '' and fecha_fin == '':
        reporte = asistencia.query.join(grupo, asistencia.id_grupo == grupo.id).filter(grupo.id_periodo == id_periodo)
        print('------------>>>>>>>>> 1:', reporte)
    ## Profesor 
    elif id_periodo == '' and id_profesor != '' and fecha_ini == '' and fecha_fin == '':
        reporte = asistencia.query.join(grupo, asistencia.id_grupo == grupo.id).filter(grupo.id_periodo == id_profesor)
        print('------------>>>>>>>>> 2:', reporte)
    ## Periodo y profesor
    elif id_periodo != '' and id_profesor != '' and fecha_ini == '' and fecha_fin == '':
        reporte = asistencia.query.join(grupo, asistencia.id_grupo == grupo.id).filter(grupo.id_periodo == id_periodo)
        print('------------>>>>>>>>> 3:', reporte)
    ## Fecha
    elif id_periodo == '' and id_profesor == '' and fecha_ini != '' and fecha_fin != '': 
        reporte = asistencia.query.filter(asistencia.fecha <= fecha_fin).filter(asistencia.fecha >= fecha_ini)
        print('---->>>>>>>>>>>>>>>> 4 Fecha:', reporte)
    ## Profesor y Fecha
    elif id_periodo == '' and id_profesor != '' and fecha_ini != '' and fecha_fin != '':
        reporte = asistencia.query.join(grupo, asistencia.id_grupo == grupo.id).filter(grupo.id_profesor == id_profesor).filter(asistencia.fecha <= fecha_fin).filter(asistencia.fecha >= fecha_ini)
        print('---->>>>>>>>>>>>>>>> 5 Profesor y fecha:', reporte)
 
    result = asistencias_esquema.dump(reporte)
    return jsonify(result)