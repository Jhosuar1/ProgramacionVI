class Antibiotico:
    def __init__(self, nombre, dosis, tipo_animal, precio):
        # Inicializa un objeto Antibiotico con nombre, dosis, tipo de animal y precio.
        self.__nombre = nombre  # Asigna el nombre del antibiótico al atributo privado __nombre.
        self.__dosis = dosis  # Asigna la dosis del antibiótico al atributo privado __dosis.
        self.__tipo_animal = tipo_animal  # Asigna el tipo de animal al que se aplica el antibiótico al atributo privado __tipo_animal.
        self.__precio = precio  # Asigna el precio del antibiótico al atributo privado __precio.

    @property
    def nombre(self):
        return self.__nombre  # Retorna el nombre del antibiótico.

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre  # Establece el nombre del antibiótico con el valor pasado como argumento.

    @property
    def dosis(self):
        return self.__dosis  # Retorna la dosis del antibiótico.

    @dosis.setter
    def dosis(self, dosis):
        self.__dosis = dosis  # Establece la dosis del antibiótico con el valor pasado como argumento.

    @property
    def tipo_animal(self):
        return self.__tipo_animal  # Retorna el tipo de animal al que se aplica el antibiótico.

    @tipo_animal.setter
    def tipo_animal(self, tipo_animal):
        self.__tipo_animal = tipo_animal  # Establece el tipo de animal al que se aplica el antibiótico con el valor pasado como argumento.

    @property
    def precio(self):
        return self.__precio  # Retorna el precio del antibiótico.

    @precio.setter
    def precio(self, precio):
        self.__precio = precio  # Establece el precio del antibiótico con el valor pasado como argumento.
