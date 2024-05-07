class ProductoControl:
    def __init__(self, registro_ICA, nombre, frecuencia_aplicacion, valor):
        self.__registro_ICA = registro_ICA  
        self.__nombre = nombre 
        self.__frecuencia_aplicacion = frecuencia_aplicacion 
        self.__valor = valor  

    @property
    def registro_ICA(self):
        return self.__registro_ICA 

    @registro_ICA.setter
    def registro_ICA(self, registro_ICA):
        self.__registro_ICA = registro_ICA 
        
    @property
    def nombre(self):
        return self.__nombre  

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre 

    @property
    def frecuencia_aplicacion(self):
        return self.__frecuencia_aplicacion  

    @frecuencia_aplicacion.setter
    def frecuencia_aplicacion(self, frecuencia_aplicacion):
        self.__frecuencia_aplicacion = frecuencia_aplicacion 

    @property
    def valor(self):
        return self.__valor 

    @valor.setter
    def valor(self, valor):
        self.__valor = valor 
