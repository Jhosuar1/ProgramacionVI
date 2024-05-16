from abc import ABC, abstractmethod
from CRUD.CRUD_Hospital import CrudHospital
from CRUD.CRUD_Doctor import CrudDoctor
from PyQt5.QtWidgets import QApplication
from GUI.interfaz import Ui_MainWindow

class Controller(ABC):
    def __init__(self):
        self.crud_hospital = CrudHospital()
        self.crud_doctor = CrudDoctor()
        self.app = QApplication([])  # Se crea la aplicación PyQt

    @abstractmethod
    def retorno_interfaz(self):
        pass

    @abstractmethod
    def llamar_interfaz_hospital(self):
        pass

    @abstractmethod
    def crear_hospital(self, nombre, id):
        pass

    @abstractmethod
    def eliminar_hospital(self, nombre):
        pass

    @abstractmethod
    def buscar_hospital(self, id):
        pass

    @abstractmethod
    def llamar_interfaz_doctor(self):
        pass

    @abstractmethod
    def crear_doctor(self, nombre, dni, especialidad, id_hospital):
        pass

    @abstractmethod
    def eliminar_doctor(self, dni):
        pass

    @abstractmethod
    def buscar_doctor(self, dni):
        pass
