class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = None

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas is not None:
            print(f"Notas: {self.notas}")

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, notas):
        self.notas = notas

def main():
    # Crear un objeto de tipo Alumno
    alumno = Alumno("Juan Pérez", "A12345")

    # Mostrar información del alumno
    alumno.display()
    
    # Asignar edad y notas al alumno
    alumno.setAge(18)
    alumno.setNota([95, 80, 85])

    # Mostrar información actualizada del alumno
    print("Información actualizada del alumno:")
    alumno.display()

if __name__ == "__main__":
    main()