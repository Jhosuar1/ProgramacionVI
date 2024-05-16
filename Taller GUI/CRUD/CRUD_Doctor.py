from abc import ABC, abstractmethod
from MODELO import Doctor

class CRUDDoctor:
    def __init__(self):
        self.doctores_registrados = []

    def crear_doctor(self, nombre, dni, especialidad, id_hospital):
        doctor = Doctor(nombre, dni, especialidad, id_hospital)
        self.doctores_registrados.append(doctor)
        return doctor

    def eliminar_doctor(self, dni):
        for doctor in self.doctores_registrados:
            if doctor.dni == dni:
                self.doctores_registrados.remove(doctor)
                return True
        return False

    def buscar_doctor(self, dni):
        for doctor in self.doctores_registrados:
            if doctor.dni == dni:
                return doctor
        return None
