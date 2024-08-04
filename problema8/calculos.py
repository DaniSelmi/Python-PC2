from problema8.operaciones import suma, resta, producto, division

def main():
    # Ejemplos de uso de las funciones
    print("Suma de 15 y 3:", suma(15, 3))
    print("Resta de 15 y 3:", resta(15, 3))
    print("Producto de 15 y 3:", producto(15, 3))
    print("División de 15 y 3:", division(15, 3))
    
    # Pruebas con errores de tipo
    print("Suma de '10' y 5:", suma("10", 5))
       
    # Prueba de división por cero
    print("División de 10 y 0:", division(10, 0))

if __name__ == "__main__":
    main()