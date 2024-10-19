from decimal import Decimal


class Transaccion:
    def __init__(self, usuario_email, activo_id, tipo, cantidad, precio, comision):
        self._usuario_email = usuario_email
        self._activo_id = activo_id
        self._tipo = tipo
        self._cantidad = cantidad
        self._precio = precio
        self._comision = comision

    @property
    def usuario_email(self):
        return self._usuario_email

    @property
    def activo_id(self):
        return self._activo_id

    @property
    def tipo(self):
        return self._tipo

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def precio(self):
        return self._precio

    @property
    def comision(self):
        return self._comision
