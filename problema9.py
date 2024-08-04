from problema3 import CIRCULO

from problema4 import RECTANGULO, CUADRADO

def validar_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("Error: El valor debe ser un número positivo.")
            else:
                return valor
        except ValueError:
            print("Error: Tipo de dato no válido. Por favor ingrese un número.")

def calcular_area_circulo():
    radio = validar_numero("Ingrese el radio del círculo: ")
    circulo = CIRCULO(radio)
    area = circulo.calcular_area()
    print(f"El área del círculo con radio {radio} es: {area:.2f}")

def calcular_area_rectangulo():
    largo = validar_numero("Ingrese el largo del rectángulo: ")
    ancho = validar_numero("Ingrese el ancho del rectángulo: ")
    rectangulo = RECTANGULO(largo, ancho)
    area = rectangulo.calcular_area()
    print(f"El área del rectángulo con largo {largo} y ancho {ancho} es: {area:.2f}")

def calcular_area_cuadrado():
    lado = validar_numero("Ingrese el lado del cuadrado: ")
    cuadrado = CUADRADO(lado)
    area = cuadrado.calcular_area()
    print(f"El área del cuadrado con lado {lado} es: {area:.2f}")

def menu():
    while True:
        print("\n--- Menú de Geometría ---")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            calcular_area_circulo()
        elif opcion == '2':
            calcular_area_rectangulo()
        elif opcion == '3':
            calcular_area_cuadrado()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    menu()