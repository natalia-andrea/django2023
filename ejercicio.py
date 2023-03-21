class Cuenta():

    def __init__(self, titular="", cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad


    #getter
    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad

    #setter
    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    def mostrar(self):
        return f"{self.titular}, {str(self.cantidad)}"

    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad

    def retirar(self, cantidad):
        self.__cantidad = self.__cantidad - cantidad    
