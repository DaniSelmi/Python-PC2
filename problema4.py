class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        super().__init__(lado, lado)

def main():
    # Crear un objeto de tipo RECTANGULO
    rectangulo = RECTANGULO(8, 12)
    
    # Crear un objeto de tipo CUADRADO
    cuadrado = CUADRADO(7)
    
    # Calcular y mostrar el área del rectángulo
    area_rectangulo = rectangulo.calcular_area()
    print(f"El área del rectángulo con largo {rectangulo.largo} y ancho {rectangulo.ancho} es: {area_rectangulo}")
    
    # Calcular y mostrar el área del cuadrado
    area_cuadrado = cuadrado.calcular_area()
    print(f"El área del cuadrado con lado {cuadrado.largo} es: {area_cuadrado}")

if __name__ == "__main__":
    main()