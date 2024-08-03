#estructura del proyecto

biblioteca/
    __init__.py
    libro.py
    gestion.py
    main.py

#archivo 'libro.py'

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}"


#archivo 'gestio.py'

from .libro import Libro

class GestionBiblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar_libros(self):
        return self.libros

    def buscar_por_titulo(self, titulo):
        return [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros if autor.lower() in libro.autor.lower()]

#archivo 'main.py'

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