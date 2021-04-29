from flask import request
from flask_restful import Resource
from wordbox.model.user import UserModel


class User(Resource):

    def get(self, id):
        try:
            user = UserModel.find_by_id(id)
            if user:
                return user.json()
            return {'message': 'User not found'}, 404
        except Exception:
            return {'message': 'Server problem'}, 500

    def post(self):
        try:
            req = request.get_json()
            telefonos = ",".join(req.get("telefonos", ""))
            user = UserModel(nombre=req.get("nombre",""),
                             apellido=req.get("apellido",""),
                             direccion=req.get("direccion",""),
                             telefonos=telefonos
                             )
            id = user.save()
            return {"id": str(id)}
        except Exception:
            return {'message': 'Server problem'}, 500
