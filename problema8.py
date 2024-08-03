def suma(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Tipo de dato no válido."

def resta(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Tipo de dato no válido."

def producto(a, b):
    try:
        return a * b
    except TypeError:
        return "Error: Tipo de dato no válido."

def division(a, b):
    try:
        return a / b
    except TypeError:
        return "Error: Tipo de dato no válido."
    except ZeroDivisionError:
        return "Error: No es posible dividir entre cero."


#ARCHIVO 'calculos.py

from operaciones import suma, resta, producto, division

def main():
    # Ejemplos de uso de las funciones
    print("Suma de 10 y 5:", suma(10, 5))
    print("Resta de 10 y 5:", resta(10, 5))
    print("Producto de 10 y 5:", producto(10, 5))
    print("División de 10 y 5:", division(10, 5))
    
    # Pruebas con errores de tipo
    print("Suma de '10' y 5:", suma("10", 5))
    print("Producto de 10 y 'cinco':", producto(10, "cinco"))
    
    # Prueba de división por cero
    print("División de 10 y 0:", division(10, 0))

if __name__ == "__main__":
    main()