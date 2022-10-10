from flask import request, jsonify, Blueprint
from sqlalchemy.orm import session 
from bioapi.schemas.periodo import periodo_esquema, periodos_esquema
from bioapi.model.periodo import periodo
from bioapi import db
from sqlalchemy import func

ruta_periodo = Blueprint('ruta-periodo', __name__)

###endponit - GET all periodo 
@ruta_periodo.route('/periodo', methods=['GET'])
def get_peridos():
    all_periodos = db.session.query(periodo)
    print(all_periodos)
    result = periodos_esquema.dump(all_periodos)
    return jsonify(result)

###endpoint - GET from ID periodo
@ruta_periodo.route('/periodo/<id>', methods=['GET'])
def get_periodo(id):
    periodo_id = periodo.query.get(id)
    result = periodo_esquema.dump(periodo_id)
    return jsonify(result)

###endpoint - GET from ID periodo -------------------------------------------------------
@ruta_periodo.route('/periodo/actual', methods=['GET'])
def get_periodo_fecha():
    maxdate = db.session.query(func.max(periodo.fecha_ini))
    periodo_id = periodo.query.filter(periodo.fecha_ini == maxdate).first()
    print('>>>>>>>>>>>>>>', periodo_id)
    result = periodo_esquema.dump(periodo_id)
    return jsonify(result)

###endpoint - POST Creacion de periodo
@ruta_periodo.route('/periodo', methods=['POST'])
def create_periodo():
    fecha_ini = request.json['fecha_ini']
    fecha_fin = request.json['fecha_fin']
    new_periodo = periodo(fecha_ini, fecha_fin)
    db.session.add(new_periodo)
    db.session.commit()
    result = periodo_esquema.dump(new_periodo)
    return jsonify(result)

###endpoint - PUT de periodo
@ruta_periodo.route('/periodo/<id>', methods=['PUT'])
def update_periodo(id):
    periodo_update = periodo.query.get(id)
    fecha_ini = request.json['fecha_ini']
    fecha_fin = request.json['fecha_fin']
    periodo_update.fecha_ini = fecha_ini
    periodo_update.fecha_fin = fecha_fin
    db.session.commit()
    result = periodo_esquema.dump(periodo_update)
    return jsonify(result)

###endpoint - DELETE periodo
@ruta_periodo.route('/periodo/<id>', methods=['DELETE'])
def delete_periodo(id):
    periodo_delete = periodo.query.get(id)
    db.session.delete(periodo_delete)
    db.session.commit()
    result = periodo_esquema.dump(periodo_delete)
    return jsonify(result)