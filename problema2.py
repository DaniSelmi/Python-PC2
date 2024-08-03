def get_grades():
    while True:
        try:
            grades_input = input("Ingrese una lista de calificaciones separadas por comas: ")
            grades_list = grades_input.split(',')
            grades = [int(grade.strip()) for grade in grades_list]
            return grades
        except ValueError:
            print("Error: Asegúrese de ingresar solo números enteros separados por comas.")

def main():
    grades = get_grades()
    print("Lista de calificaciones:", grades)

if __name__ == "__main__":
    main()