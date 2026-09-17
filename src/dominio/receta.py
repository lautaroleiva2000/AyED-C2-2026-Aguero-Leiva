CATALOGO = [
    {"id": 1, "nombre": "Chimichurri", "tiempo_min": 15, "dificultad": "baja"},
    {"id": 2, "nombre": "Salsa criolla", "tiempo_min": 20, "dificultad": "baja"},
    {"id": 3, "nombre": "Sofrito", "tiempo_min": 25, "dificultad": "baja"},
]


class Receta:
    def __init__(self, id_receta, nombre, tiempo_min, dificultad):
        self.id = id_receta
        self.nombre = nombre
        self.tiempo_min = tiempo_min
        self.dificultad = dificultad

    def resumen(self):
        return f"{self.id}. {self.nombre} - {self.tiempo_min} min - Dificultad: {self.dificultad}"
