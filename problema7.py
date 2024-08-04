import math

### Clase Punto

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "I Cuadrante"
        elif self.x < 0 and self.y > 0:
            return "II Cuadrante"
        elif self.x < 0 and self.y < 0:
            return "III Cuadrante"
        elif self.x > 0 and self.y < 0:
            return "IV Cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
        else:
            return "En el origen"

    def vector(self, otro_punto):
        return (otro_punto.x - self.x, otro_punto.y - self.y)

    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)

### Clase Rectangulo

class Rectangulo:
    def __init__(self, punto1=Punto(), punto2=Punto()):
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return abs(self.punto2.x - self.punto1.x)

    def altura(self):
        return abs(self.punto2.y - self.punto1.y)

    def area(self):
        return self.base() * self.altura()

### Experimentación

# Creación de los puntos
A = Punto(3, 5)
B = Punto(6, 6)
C = Punto(-8, -5)
D = Punto(0, 0)

# Impresión de los puntos
print("Punto A:", A)
print("Punto B:", B)
print("Punto C:", C)
print("Punto D:", D)

# Consulta de cuadrantes
print("Cuadrante del punto A:", A.cuadrante())
print("Cuadrante del punto C:", C.cuadrante())
print("Cuadrante del punto D:", D.cuadrante())

# Consulta de vectores
print("Vector AB:", A.vector(B))
print("Vector BA:", B.vector(A))

# Consulta de distancias (opcional)
print("Distancia entre A y B:", A.distancia(B))
print("Distancia entre B y A:", B.distancia(A))

# Determinar el punto más lejos del origen
distancia_A = A.distancia(D)
distancia_B = B.distancia(D)
distancia_C = C.distancia(D)

print("Distancia del punto A al origen:", distancia_A)
print("Distancia del punto B al origen:", distancia_B)
print("Distancia del punto C al origen:", distancia_C)

if distancia_A > distancia_B and distancia_A > distancia_C:
    print("El punto A está más lejos del origen.")
elif distancia_B > distancia_A and distancia_B > distancia_C:
    print("El punto B está más lejos del origen.")
else:
    print("El punto C está más lejos del origen.")

# Creación del rectángulo utilizando los puntos A y B
rectangulo = Rectangulo(A, B)

# Consulta de la base, altura y área del rectángulo
print("Base del rectángulo:", rectangulo.base())
print("Altura del rectángulo:", rectangulo.altura())
print("Área del rectángulo:", rectangulo.area())