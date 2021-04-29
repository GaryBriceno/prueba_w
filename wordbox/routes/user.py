from flask import request
from flask_restful import Resource
from wordbox.model.user import UserModel


class User(Resource):

    def get(self, id):
        user = UserModel.find_by_id(id)
        if user:
            return user.json()
        return {'message': 'User not found'}, 404

    def post(self):
        req = request.get_json()
        user = UserModel(nombre=req.get("nombre",""),
                         apellido=req.get("apellido",""),
                         direccion=req.get("direccion","")
                         )
        id = user.save()

        return {"id": str(id)}