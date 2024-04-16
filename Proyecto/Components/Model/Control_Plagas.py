from Model.ProductoControl import ProductoControl

class ControlPlagas(ProductoControl):
    def __init__(self, registro_ICA, nombre, frecuencia_aplicacion, valor, periodo_carencia):
        super().__init__(registro_ICA, nombre, frecuencia_aplicacion, valor)
        self.__periodo_carencia = periodo_carencia

    @property
    def periodo_carencia(self):
        return self.__periodo_carencia

    @periodo_carencia.setter
    def periodo_carencia(self, periodo_carencia):
        self.__periodo_carencia = periodo_carencia
