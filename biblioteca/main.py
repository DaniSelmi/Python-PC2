from biblioteca.libro import Libro
from biblioteca.gestion import GestionBiblioteca

def mostrar_menu():
    print("\n--- Menú de Gestión de Biblioteca ---")
    print("1. Agregar un libro a la biblioteca")
    print("2. Listar los libros en la biblioteca")
    print("3. Buscar un libro por título")
    print("4. Buscar un libro por autor")
    print("5. Salir")

def agregar_libro(biblioteca):
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    isbn = input("Ingrese el ISBN del libro: ")
    libro = Libro(titulo, autor, isbn)
    biblioteca.agregar_libro(libro)
    print("Libro agregado correctamente.")

def listar_libros(biblioteca):
    libros = biblioteca.listar_libros()
    if not libros:
        print("La biblioteca no tiene libros.")
    else:
        for libro in libros:
            print(libro)

def buscar_por_titulo(biblioteca):
    titulo = input("Ingrese el título del libro que desea buscar: ")
    libros = biblioteca.buscar_por_titulo(titulo)
    if not libros:
        print(f"No se encontraron libros con el título '{titulo}'.")
    else:
        for libro in libros:
            print(libro)

def buscar_por_autor(biblioteca):
    autor = input("Ingrese el autor del libro que desea buscar: ")
    libros = biblioteca.buscar_por_autor(autor)
    if not libros:
        print(f"No se encontraron libros del autor '{autor}'.")
    else:
        for libro in libros:
            print(libro)

def main():
    biblioteca = GestionBiblioteca()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_libro(biblioteca)
        elif opcion == '2':
            listar_libros(biblioteca)
        elif opcion == '3':
            buscar_por_titulo(biblioteca)
        elif opcion == '4':
            buscar_por_autor(biblioteca)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()