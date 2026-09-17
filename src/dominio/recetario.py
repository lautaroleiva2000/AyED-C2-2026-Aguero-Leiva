from src.dominio.receta import Receta, CATALOGO


class Recetario:
    def __init__(self):
        self.recetas = []

        for datos in CATALOGO:
            receta = Receta(
                datos["id"],
                datos["nombre"],
                datos["tiempo_min"],
                datos["dificultad"]
            )
            self.recetas.append(receta)

    def listar_catalogo(self):
        for receta in self.recetas:
            print(receta.resumen())

    def buscar_receta(self, id_receta):
        for receta in self.recetas:
            if receta.id == id_receta:
                return receta
        return None
