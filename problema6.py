class Producto:
    def __init__(self, nombre, precio, año, marca):
        self.nombre = nombre
        self.precio = precio
        self.año = año
        self.marca = marca

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: ${self.precio}, Año: {self.año}, Marca: {self.marca}"

class Catálogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if not self.productos:
            print("El catálogo está vacío.")
        else:
            for producto in self.productos:
                print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        return productos_filtrados

    def buscar_por_marca(self, marca):
        productos_encontrados = [producto for producto in self.productos if producto.marca.lower() == marca.lower()]
        return productos_encontrados

def main():
    # Crear objetos de tipo Producto
    producto1 = Producto("Filtro de aceite", 15.99, 2020, "Bosch")
    producto2 = Producto("Batería", 120.50, 2022, "Exide")
    producto3 = Producto("Neumático", 75.00, 2021, "Michelin")

    # Crear objeto de tipo Catálogo
    catalogo = Catálogo()

    # Agregar productos al catálogo
    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)

    # Mostrar todos los productos en el catálogo
    print("Todos los productos en el catálogo:")
    catalogo.mostrar_productos()

    # Filtrar productos por año
    año_filtrar = 2021
    productos_filtrados = catalogo.filtrar_por_año(año_filtrar)
    print(f"\nProductos del año {año_filtrar}:")
    for producto in productos_filtrados:
        print(producto)

    # Buscar productos por marca
    marca_buscar = "Bosch"
    productos_encontrados = catalogo.buscar_por_marca(marca_buscar)
    print(f"\nProductos de la marca {marca_buscar}:")
    for producto in productos_encontrados:
        print(producto)

if __name__ == "__main__":
    main()