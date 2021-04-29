from wordbox.model.user import UserModel


def test_new_user():
    user = UserModel(nombre="Juan", apellido="Perez", direccion="Medellin", telefonos="")

    assert user.nombre == "Juan"
    assert user.apellido == "Perez"
    assert user.direccion == "Medellin"
    assert user.telefonos == ""
