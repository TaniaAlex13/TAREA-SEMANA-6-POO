# Clase Producto con Descuento
# Hereda de la clase abstracta Producto

from modelos.producto import Producto

class ProductoConDescuento(Producto):
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio)
        self.descuento = descuento

    # Implementación obligatoria del método abstracto
    def calcular_precio_final(self):
        return self.get_precio() * (1 - self.descuento)