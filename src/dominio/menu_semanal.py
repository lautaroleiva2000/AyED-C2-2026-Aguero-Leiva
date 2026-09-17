class MenuSemanal:
    def __init__(self):
        self.recetas = []

    def agregar_receta(self, dia, receta):
        self.recetas.append((dia, receta))

    def listar_menu(self):
        return [
            f"{dia}: {receta.nombre}"
            for dia, receta in self.recetas
        ]
