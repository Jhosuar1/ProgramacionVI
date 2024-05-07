from Model.ProductoControl import ProductoControl  # Importa la clase ProductoControl del módulo Model.ProductoControl

class ControlPlagas(ProductoControl):  # Define una nueva clase llamada ControlPlagas que hereda de ProductoControl
    def __init__(self, registro_ICA, nombre, frecuencia_aplicacion, valor, periodo_carencia):
        super().__init__(registro_ICA, nombre, frecuencia_aplicacion, valor)  # Llama al constructor de la clase padre ProductoControl
        self.__periodo_carencia = periodo_carencia  # Inicializa el atributo privado __periodo_carencia con el valor recibido como argumento

    @property  # Define un método periodo_carencia como una propiedad de solo lectura
    def periodo_carencia(self):
        return self.__periodo_carencia  # Retorna el valor del atributo privado __periodo_carencia

    @periodo_carencia.setter  # Define un método setter para la propiedad periodo_carencia
    def periodo_carencia(self, periodo_carencia):
        self.__periodo_carencia = periodo_carencia  # Establece el valor del atributo privado __periodo_carencia con el valor recibido
