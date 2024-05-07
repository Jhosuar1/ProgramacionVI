from Model.Factura import Factura  

class Cliente:
    def __init__(self, nombre, cedula):
        self.__nombre = nombre  
        self.__cedula = cedula  
        self.__facturas = []  
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

    def generar_factura(self, fecha, valor_total):
        factura = Factura(fecha, valor_total)  # Creamos una nueva instancia de Factura con la fecha y valor total dados
        self.__facturas.append(factura) 
        return factura

    def obtener_facturas(self):
        return self.__facturas 
