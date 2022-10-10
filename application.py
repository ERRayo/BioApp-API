from bioapi import app
from bioapi.config.default import configApp

if __name__=="__main__":  
    app.config.from_object(configApp['development'])
    app.run(host='0.0.0.0')