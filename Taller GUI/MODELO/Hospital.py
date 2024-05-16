class Hospital:
    def __init__(self, nombre, id):
        self._nombre = nombre
        self._id = id
        self._doctores = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def id(self):
        return self._id

    @property
    def doctores(self):
        return self._doctores

    def agregar_doctor(self, doctor):
        self._doctores.append(doctor)

    def eliminar_doctor(self, doctor):
        self._doctores.remove(doctor)