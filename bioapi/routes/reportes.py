from flask import request, jsonify, Blueprint
from sqlalchemy import func
from sqlalchemy.orm import session
from sqlalchemy.sql.functions import count 
from bioapi import db


ruta_reportes = Blueprint('ruta_reportes', __name__)

