class ProductoControl:
    def __init__(self, registro_ICA, nombre, frecuencia_aplicacion, valor):
        self.__registro_ICA = registro_ICA  # Asigna el valor de registro_ICA al atributo privado __registro_ICA
        self.__nombre = nombre  # Asigna el valor de nombre al atributo privado __nombre
        self.__frecuencia_aplicacion = frecuencia_aplicacion  # Asigna el valor de frecuencia_aplicacion al atributo privado __frecuencia_aplicacion
        self.__valor = valor  # Asigna el valor de valor al atributo privado __valor

    @property
    def registro_ICA(self):
        return self.__registro_ICA  # Retorna el valor del atributo privado __registro_ICA cuando se accede a través del método registro_ICA

    @registro_ICA.setter
    def registro_ICA(self, registro_ICA):
        self.__registro_ICA = registro_ICA  # Establece el valor del atributo privado __registro_ICA cuando se establece a través del método registro_ICA

    @property
    def nombre(self):
        return self.__nombre  # Retorna el valor del atributo privado __nombre cuando se accede a través del método nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre  # Establece el valor del atributo privado __nombre cuando se establece a través del método nombre

    @property
    def frecuencia_aplicacion(self):
        return self.__frecuencia_aplicacion  # Retorna el valor del atributo privado __frecuencia_aplicacion cuando se accede a través del método frecuencia_aplicacion

    @frecuencia_aplicacion.setter
    def frecuencia_aplicacion(self, frecuencia_aplicacion):
        self.__frecuencia_aplicacion = frecuencia_aplicacion  # Establece el valor del atributo privado __frecuencia_aplicacion cuando se establece a través del método frecuencia_aplicacion

    @property
    def valor(self):
        return self.__valor  # Retorna el valor del atributo privado __valor cuando se accede a través del método valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor  # Establece el valor del atributo privado __valor cuando se establece a través del método valor
