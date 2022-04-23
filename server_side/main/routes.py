from . import app, db
from .models import Names
from flask_restful import Api, Resource, abort, marshal_with, reqparse, fields

api = Api(app)

name_put_args = reqparse.RequestParser()
name_put_args.add_argument("name", type=str, help="Name not sent", required=True)
name_put_args.add_argument("age", type=int, help="Age not sent")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'age': fields.Integer
}

class Name(Resource):
    @marshal_with(resource_fields)
    def get(self, name_id):
        result = Names.query.filter_by(id=name_id).first()
        if not result:
            abort(404, message="Couldn't find the result")
        return result

    @marshal_with(resource_fields)
    def put(self, name_id):
        args = name_put_args.parse_args()

        result = Names.query.filter_by(id=name_id).first()
        if result:
            abort(409, message="id already exists")

        name = Names(
            id = name_id,
            name = args['name'],
            age = args['age']
        )

        db.session.add(name)
        db.session.commit()
        return name, 201        

api.add_resource(Name, "/api/<int:name_id>")