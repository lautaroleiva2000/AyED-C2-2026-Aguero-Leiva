import csv


def cargar_csv(ruta):
    """Carga secuencial. Devuelve una lista de dicts (E1 puede quedar así)."""
    filas = []

    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            filas.append(fila)

    return filas


def guardar_csv(ruta, filas, encabezados):
    raise NotImplementedError
