from src.tads.nodo import Nodo

class ListaEnlazada:
    """Lista enlazada simple propia con nodos (sin usar list de Python)."""
    def __init__(self):
        self._cabeza = None
        self._tamanio = 0

    def esta_vacia(self):
        return self._cabeza is None

    def tamanio(self):
        return self._tamanio

    def insertar_al_inicio(self, dato):
        self._cabeza = Nodo(dato, self._cabeza)
        self._tamanio += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self._cabeza = nuevo
        else:
            actual = self._cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

    def buscar(self, dato):
        actual = self._cabeza
        while actual is not None:
            if actual.dato == dato:
                return actual
            actual = actual.siguiente
        return None

    def eliminar(self, dato):
        if self.esta_vacia():
            return

        # Caso 1: el dato está en la cabeza
        if self._cabeza.dato == dato:
            self._cabeza = self._cabeza.siguiente
            self._tamanio -= 1
            return

        # Caso 2: buscar el nodo en el medio o final
        actual = self._cabeza
        while actual.siguiente is not None:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                self._tamanio -= 1
                return
            actual = actual.siguiente

    def __iter__(self):
        """Iterador para recorrer la lista con 'for elemento in lista'."""
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente
