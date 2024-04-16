class Cliente:
    def __init__(self, nombre, cedula):
        self.__nombre = nombre
        self.__cedula = cedula

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, cedula):
        self.__cedula = cedula
