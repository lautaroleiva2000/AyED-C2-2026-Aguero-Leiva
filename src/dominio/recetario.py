from src.dominio.receta import Receta, CATALOGO
from src.tads.lista_enlazada import ListaEnlazada


class Recetario:
    def __init__(self):
        self.recetas = ListaEnlazada()

        self.relaciones = {
            10: [3, 5]
        }

        for datos in CATALOGO:
            receta = Receta(
                datos["id"],
                datos["nombre"],
                datos["tiempo_min"],
                datos["dificultad"]
            )
            self.recetas.insertar_al_final(receta)

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
