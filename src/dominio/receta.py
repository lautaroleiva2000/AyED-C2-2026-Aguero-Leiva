CATALOGO = [
    {"id": 1, "nombre": "Chimichurri", "tiempo_min": 15, "dificultad": "baja", "categoria": "salsa"},
    {"id": 2, "nombre": "Salsa criolla", "tiempo_min": 20, "dificultad": "baja", "categoria": "salsa"},
    {"id": 3, "nombre": "Sofrito", "tiempo_min": 25, "dificultad": "baja", "categoria": "base"},
    {"id": 5, "nombre": "Masa de empanadas", "tiempo_min": 90, "dificultad": "media", "categoria": "masa"},
    {"id": 10, "nombre": "Empanadas de carne", "tiempo_min": 150, "dificultad": "media", "categoria": "principal"},
]


class Receta:
    def __init__(self, id_receta, nombre, tiempo_min, dificultad, categoria=""):
        self.id = id_receta
        self.nombre = nombre
        self.tiempo_min = tiempo_min
        self.dificultad = dificultad
        self.categoria = categoria

    def resumen(self):
        return f"{self.id}. {self.nombre} - {self.tiempo_min} min - Dificultad: {self.dificultad}"
