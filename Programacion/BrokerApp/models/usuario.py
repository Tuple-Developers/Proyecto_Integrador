class Usuario:
    def __init__(self, email, cuil, nombre, apellido, password, saldo):
        self._email = email
        self._cuil = cuil
        self._nombre = nombre
        self._apellido = apellido
        self._password = password
        self._saldo = saldo

    @property
    def email(self):
        return self._email

    @property
    def cuil(self):
        return self._cuil

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def password(self):
        return self._password

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        self._saldo = value