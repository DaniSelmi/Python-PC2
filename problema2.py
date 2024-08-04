def conseguir_notas():
    while True:
        try:
            notas = input("Ingrese una lista de calificaciones separadas por comas: ")
            lista_notas = notas.split(',')

            grades = [int(grade.strip()) for grade in lista_notas]
            return grades
        except ValueError:
            print("Error: Asegúrese de ingresar solo números enteros separados por comas.")

def main():
    grades = conseguir_notas()
    print("Lista de calificaciones:", grades)

if __name__ == "__main__":
    main()