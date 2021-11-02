from flask import Flask
from flask_restx import Api
from flask_cors import CORS

from config import Configurations
from app.blueprints import BlueprintCreator

CONFIG = Configurations.get_configuarations()

class AppInitializer():
    '''
        Building plan for the Flask-restx REST API. This class defines the app and api objects

        attributes:
            none

        methods:
            createApp: 
                Entrypoint and initialisation class of the app and api object. 
    '''

    def createApp():
        '''
            This function is the entrypoint to the REST API. It instanziates the Python Flask app
            as well as the Flask_restx REST-API
        
            Parameter:
                None
            Returns:
                app: The Python Flask object
        '''

        db_query = BlueprintCreator.create_blueprint()
        config = Configurations.get_configuarations()
        app = Flask(__name__)
        app.register_blueprint(db_query, url_prefix='/api/')
        app.config['DEBUG'] = True
        app.config["APPLICATION_ROOT"] = "/api" #TODO #1
        
        CORS(app, resources=CONFIG["CORS"])

        # add Namespaces
        return app


if __name__ == '__main__':
    app = AppInitializer.createApp()
    app.run(port=CONFIG["PORT"])
