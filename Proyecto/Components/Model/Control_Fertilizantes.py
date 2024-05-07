from Model.ProductoControl import ProductoControl  

class ControlFertilizantes(ProductoControl): 
    def __init__(self, registro_ICA, nombre, frecuencia_aplicacion, valor, fecha_ultima_aplicacion):
        super().__init__(registro_ICA, nombre, frecuencia_aplicacion, valor)  # Llama al constructor de la clase padre ProductoControl
        self.__fecha_ultima_aplicacion = fecha_ultima_aplicacion  

    @property
    def fecha_ultima_aplicacion(self):  
        return self.__fecha_ultima_aplicacion

    @fecha_ultima_aplicacion.setter 
    def fecha_ultima_aplicacion(self, fecha_ultima_aplicacion):
        self.__fecha_ultima_aplicacion = fecha_ultima_aplicacion  
