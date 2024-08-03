import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

def main():
    # Crear dos objetos de tipo CIRCULO
    circulo1 = CIRCULO(5)
    circulo2 = CIRCULO(10)
    
    # Calcular y mostrar el área de los dos círculos
    area1 = circulo1.calcular_area()
    area2 = circulo2.calcular_area()
    
    print(f"El área del círculo con radio {circulo1.radio} es: {area1:.2f}")
    print(f"El área del círculo con radio {circulo2.radio} es: {area2:.2f}")

if __name__ == "__main__":
    main()