

from flask_restx import Namespace, Resource

namespace = Namespace("queryZenodo", description="Route to query SabioRK")


@namespace.route("")
class QuerySabioRK(Resource):
    @namespace.doc()
    def post(self):
        print("hallo Welt")