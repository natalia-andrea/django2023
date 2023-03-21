#Ejercicio 7

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
  


#Ejercicio 8

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        Cuenta.__init__(self, titular, cantidad)
        self.__bonificacion = bonificacion

    #getter
    @property
    def bonificacion(self):
        return self.__bonificacion

    #setter
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion


    def es_titular_valido(self):
        return self.titular.edad >= 18 and self.titular.edad < 25


    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)

    def mostrar(self):
        return f"Cuenta Joven {self.bonificacion}"
 

