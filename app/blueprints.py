from flask import Blueprint
from flask_restx import Api

from app.sabio_rk.sabio_rk_adapter import namespace as sabio_rk



class BlueprintCreator:
    '''
        Sets upt the blueprint for the python flask package. 

        attr:
            None
        
        methods:
            create_blueprints
    '''

    def create_blueprint():
        db_query = Blueprint('db_query', __name__)
        api = Api(db_query)
        api.add_namespace(sabio_rk, "sabio-Rk")
        return db_query

