from wordbox.model.db import db


class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(60))
    apellido = db.Column(db.String(60))
    direccion = db.Column(db.String(60))
    telefonos = db.Column(db.String(300))

    def __init__(self, nombre, apellido, direccion, telefonos):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefonos = telefonos

    def save(self):
        db.session.add(self)
        db.session.flush()
        db.session.refresh(self)
        db.session.commit()
        return self.id

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def json(self):
        return {"nombre":self.nombre,
                "apellido": self.apellido,
                "direccion": self.direccion,
                "telefonos": self.telefonos.split(",")}