class DevelopmentConfig():
    DEBUG = True

class ConexionDBConfig():
    MySQL_HOST = 'localhost' 
    mySQL_PORT = '3306'
    MySQL_USER = 'root'
    MySQL_PASSWORD = 'admin'
    MySQL_DB = 'biodb'

    SECRET_KEY = 'Test'
    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + MySQL_USER + ':' + MySQL_PASSWORD + '@' + MySQL_HOST + ':' + mySQL_PORT + '/' + MySQL_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False

configApp = {
    'development': DevelopmentConfig
}

configConexion = {
    'conexionDB': ConexionDBConfig
}
