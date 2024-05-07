from Model.ProductoControl import ProductoControl  # Importa la clase ProductoControl del módulo Model.ProductoControl

class ControlFertilizantes(ProductoControl):  # Define una nueva clase ControlFertilizantes que hereda de ProductoControl
    def __init__(self, registro_ICA, nombre, frecuencia_aplicacion, valor, fecha_ultima_aplicacion):
        super().__init__(registro_ICA, nombre, frecuencia_aplicacion, valor)  # Llama al constructor de la clase padre ProductoControl
        self.__fecha_ultima_aplicacion = fecha_ultima_aplicacion  # Inicializa el atributo privado __fecha_ultima_aplicacion

    @property
    def fecha_ultima_aplicacion(self):  # Define un método para obtener el valor del atributo __fecha_ultima_aplicacion
        return self.__fecha_ultima_aplicacion

    @fecha_ultima_aplicacion.setter  # Define un método para modificar el valor del atributo __fecha_ultima_aplicacion
    def fecha_ultima_aplicacion(self, fecha_ultima_aplicacion):
        self.__fecha_ultima_aplicacion = fecha_ultima_aplicacion  # Asigna un nuevo valor al atributo __fecha_ultima_aplicacion
