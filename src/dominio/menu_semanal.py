from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColeccionLlenaError, ItemNoEncontradoError

class MenuSemanal:
    """Colección principal del dominio sobre ListaEnlazada con tope máximo."""
    def __init__(self, tope=6):
        self._recetas = ListaEnlazada()
        self._tope = tope

    def agregar(self, receta):
        """Agrega una receta. Si supera el tope, lanza ColeccionLlenaError."""
        if self._recetas.tamanio() >= self._tope:
            raise ColeccionLlenaError(f"El menú semanal está lleno (máximo {self._tope} recetas).")
        self._recetas.insertar_al_final(receta)

    def eliminar(self, receta):
        """Elimina una receta del menú semanal."""
        if self._recetas.buscar(receta) is None:
            raise ItemNoEncontradoError("La receta no se encuentra en el menú semanal.")
        self._recetas.eliminar(receta)

    def esta_lleno(self):
        return self._recetas.tamanio() >= self._tope

    def esta_vacio(self):
        return self._recetas.esta_vacia()

    def __iter__(self):
        """Permite recorrer el menú con 'for receta in menu' usando el iterador de ListaEnlazada."""
        return iter(self._recetas)
