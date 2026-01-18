# Archivo principal

from modelos.producto_descuento import ProductoConDescuento
from servicios.tienda import Tienda

# Crear tienda
tienda = Tienda()

# Crear productos (NO se puede crear Producto directamente)
producto1 = ProductoConDescuento("Camisa", 20.00, 0.10)
producto2 = ProductoConDescuento("Zapatos", 50.00, 0.20)

# Agregar productos
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)

# Mostrar productos
tienda.mostrar_productos()
