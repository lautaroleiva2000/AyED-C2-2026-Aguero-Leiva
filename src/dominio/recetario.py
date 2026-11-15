from src.dominio.receta import Receta, CATALOGO
from src.tads.lista_enlazada import ListaEnlazada


class Recetario:
    def __init__(self, cargar_catalogo=True):
        self.recetas = ListaEnlazada()

        self.relaciones = {
            10: [3, 5]
        }

        if cargar_catalogo:
            for datos in CATALOGO:
                receta = Receta(
                    datos["id"],
                    datos["nombre"],
                    datos["tiempo_min"],
                    datos["dificultad"]
                )
                self.recetas.insertar_al_final(receta)

    def tamanio(self):
        return self.recetas.tamanio()

    def __iter__(self):
        return iter(self.recetas)

    def listar_catalogo(self):
        for receta in self.recetas:
            print(receta.resumen())

    def buscar_receta(self, id_receta):
        for receta in self.recetas:
            if receta.id == id_receta:
                return receta
        return None

    def buscar_por_nombre(self, nombre):
        for receta in self.recetas:
            if receta.nombre.lower() == nombre.lower():
                return receta
        return None

    def subrecetas(self, id_receta):
        return self.relaciones.get(id_receta, [])

    def desglosar_subrecetas(self, id_receta):
        sub = self.subrecetas(id_receta)

        if not sub:
            return [id_receta]

        resultado = [id_receta]

        for s in sub:
            resultado += self.desglosar_subrecetas(s)

        return resultado

    def insertar_al_final(self, receta):
        self.recetas.insertar_al_final(receta)

    def posicion_del_id(self, id_receta):
        for posicion, receta in enumerate(self.recetas):
            if receta.id == id_receta:
                return posicion
        return None

    def eliminar_receta(self, receta):
        self.recetas.eliminar(receta)
