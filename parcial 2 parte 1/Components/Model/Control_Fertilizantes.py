from .ProductoControl import ProductoControl

class ControlFertilizantes(ProductoControl):
    def __init__(self, registro_ICA, nombre, frecuencia_aplicacion, valor, fecha_ultima_aplicacion):
        super().__init__(registro_ICA, nombre, frecuencia_aplicacion, valor)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion
