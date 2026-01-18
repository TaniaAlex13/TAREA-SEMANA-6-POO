# Clase Tienda
# Maneja la lógica del sistema para tienda

class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(
                f"Producto: {producto.get_nombre()} | "
                f"Precio final: ${producto.calcular_precio_final():.2f}"
            )
