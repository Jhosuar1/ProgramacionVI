from MODELO import Hospital

class CRUDHospital:
    def __init__(self):
        self.hospitales_registrados = []

    def crear_hospital(self, nombre, id):
        hospital = Hospital(nombre, id)
        self.hospitales_registrados.append(hospital)
        return hospital

    def eliminar_hospital(self, nombre):
        for hospital in self.hospitales_registrados:
            if hospital.nombre == nombre:
                self.hospitales_registrados.remove(hospital)
                return True
        return False

    def buscar_hospital(self, id):
        for hospital in self.hospitales_registrados:
            if hospital.id == id:
                return hospital
        return None
