from Model.Factura import Factura  # Importamos la clase Factura

class Cliente:
    def __init__(self, nombre, cedula):
        self.__nombre = nombre  # Asignamos el nombre del cliente
        self.__cedula = cedula  # Asignamos la cedula del cliente
        self.__facturas = []  # Inicializamos una lista para almacenar las facturas del cliente

    @property
    def nombre(self):
        return self.__nombre  # Devolvemos el nombre del cliente

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre  # Asignamos un nuevo nombre al cliente

    @property
    def cedula(self):
        return self.__cedula  # Devolvemos la cedula del cliente

    @cedula.setter
    def cedula(self, cedula):
        self.__cedula = cedula  # Asignamos una nueva cedula al cliente

    def generar_factura(self, fecha, valor_total):
        factura = Factura(fecha, valor_total)  # Creamos una nueva instancia de Factura con la fecha y valor total dados
        self.__facturas.append(factura)  # Agregamos la factura a la lista de facturas del cliente
        return factura  # Devolvemos la factura generada

    def obtener_facturas(self):
        return self.__facturas  # Devolvemos la lista de facturas del cliente