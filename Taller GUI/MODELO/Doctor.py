class Doctor:
    def __init__(self, nombre, dni, especialidad, id_hospital):
        self._nombre = nombre
        self._dni = dni
        self._especialidad = especialidad
        self._id_hospital = id_hospital

    @property
    def nombre(self):
        return self._nombre

    @property
    def dni(self):
        return self._dni

    @property
    def especialidad(self):
        return self._especialidad

    @property
    def id_hospital(self):
        return self._id_hospital