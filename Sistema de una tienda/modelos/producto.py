# Clase abstracta Producto
# Usa el módulo abc para definir métodos obligatorios

from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio):
        self.__nombre = nombre      # Encapsulación
        self.__precio = precio

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    # Método abstracto (obligatorio para las clases hijas)
    @abstractmethod
    def calcular_precio_final(self):
        pass
