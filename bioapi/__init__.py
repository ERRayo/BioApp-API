import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from bioapi.config.default import configConexion
from flask_jwt_extended import JWTManager
from bioapi.constants.http_status_codes import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from flasgger import Swagger, swag_from
#from bioapi.config.swagger import template, swagger_config
from flask_cors import CORS, cross_origin


application = app = Flask(__name__,instance_relative_config=True)

cors = CORS(app, resources={r'*': {'origins':'*'}})


app.config.from_mapping(SECRET_KEY=os.environ.get('SECRET_KEY'), JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY'), 
                        SWAGGER={
                            'title': "BioAPP API",
                            'uiversion': 3
                        }
                        )

app.config.from_object(configConexion['conexionDB'])
app.config['RESTPLUS_MASK_SWAGGER'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


JWTManager(app)

from bioapi.routes.asistencia import ruta_asistencia
from bioapi.routes.carrera import ruta_carrera
from bioapi.routes.grupo import ruta_grupo
from bioapi.routes.horario import ruta_horario
from bioapi.routes.huella_profesor import ruta_huella
from bioapi.routes.materia import ruta_materia
from bioapi.routes.periodo import ruta_periodo
from bioapi.routes.prefecto import ruta_prefecto
from bioapi.routes.profesor import ruta_profesor
from bioapi.routes.usuario import ruta_usuario
from bioapi.routes.reportes import ruta_reportes
from bioapi.routes.auth import auth

app.register_blueprint(ruta_asistencia)
app.register_blueprint(ruta_carrera)
app.register_blueprint(ruta_grupo)
app.register_blueprint(ruta_horario)
app.register_blueprint(ruta_huella)
app.register_blueprint(ruta_materia)
app.register_blueprint(ruta_periodo)
app.register_blueprint(ruta_prefecto)
app.register_blueprint(ruta_profesor)
app.register_blueprint(ruta_usuario)
app.register_blueprint(ruta_reportes)
app.register_blueprint(auth)

#Swagger(app, config=swagger_config, template=template)


@app.errorhandler(HTTP_404_NOT_FOUND)
def handel_404(e):
    return jsonify({'error': 'Not found'}), HTTP_404_NOT_FOUND

@app.errorhandler(HTTP_500_INTERNAL_SERVER_ERROR)
def handle_500(e):
    return jsonify({'error': 'Something went wrong, we are working on it'}), HTTP_500_INTERNAL_SERVER_ERROR