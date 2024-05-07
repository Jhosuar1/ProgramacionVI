class Factura:
    def __init__(self, fecha, valor_total):
        self.__fecha = fecha  
        self.__valor_total = valor_total  
        self.__productos_comprados = [] 

    @property
    def fecha(self):
        return self.__fecha 

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha 
        

    @property
    def valor_total(self):
        return self.__valor_total 
        

    @valor_total.setter
    def valor_total(self, valor_total):
        self.__valor_total = valor_total 

    def agregar_producto(self, producto):
        self.__productos_comprados.append(producto)

    def obtener_productos(self):
        return self.__productos_comprados
        

    
