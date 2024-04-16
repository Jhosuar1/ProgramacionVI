class Pedido:
    def __init__(self, fecha_entrega, valor_total):
        self.__fecha_entrega = fecha_entrega
        self.__valor_total = valor_total
        self.__productos_comprados = []

    @property
    def fecha_entrega(self):
        return self.__fecha_entrega

    @fecha_entrega.setter
    def fecha_entrega(self, fecha_entrega):
        self.__fecha_entrega = fecha_entrega

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

