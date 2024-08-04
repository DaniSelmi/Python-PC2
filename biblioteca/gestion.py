from biblioteca.libro import Libro

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