class Configurations:
    '''
    Stores the configurations for the Flask_restx REST API, in particular it stores the params for:
    - CORS
    - PORT
    - DEBUG Mode

    Methods
        compiles and returns the configuaration parameter for the flask_restx REST-API in the config dict
    '''

    def get_configuarations():
        '''
        Return the config Dict which holds the config params for the flask-retx REST-API

        Params: 
            None

        Returns:
            config:dict dictionary containing the flask config params (CORS, port, debug mode)
        '''
        config = {
            "CORS":{r'/api/*':{'origins':'*'}},
            "PORT":8000,
            "DEBUG":True
                }
        return config