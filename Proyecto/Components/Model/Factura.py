class Factura:
    def __init__(self, fecha, valor_total):# Inicializa una instancia de Factura con una fecha y un valor total
        self.__fecha = fecha  # Asigna la fecha a un atributo privado
        self.__valor_total = valor_total  # Asigna el valor total a un atributo privado
        self.__productos_comprados = []  # Inicializa una lista vacía para almacenar los productos comprados

    @property
    def fecha(self):
        return self.__fecha # Método getter para obtener la fecha de la factura

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha # Método setter para actualizar la fecha de la factura
        

    @property
    def valor_total(self):
        return self.__valor_total # Método getter para obtener el valor total de la factura
        

    @valor_total.setter
    def valor_total(self, valor_total):
        self.__valor_total = valor_total # Método setter para actualizar el valor total de la factura

    def agregar_producto(self, producto):
        self.__productos_comprados.append(producto) # Método para agregar un producto a la lista de productos comprados

    def obtener_productos(self):
        return self.__productos_comprados# Método para obtener la lista de productos comprados
        

    