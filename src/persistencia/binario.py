import struct
from src.excepciones import ArchivoInvalidoError
from src.dominio.receta import Receta
from src.dominio.recetario import Recetario


FORMATO = struct.Struct("<I 30s H 10s 15s")
HEADER = struct.Struct("<4s 1s I")
TEMA = b"R"


def _a_bytes(texto, ancho):
    """Convierte texto a bytes de longitud fija."""
    return texto.encode("utf-8")[:ancho].ljust(ancho, b"\x00")


def _a_texto(datos):
    """Convierte bytes de longitud fija nuevamente a texto."""
    return datos.rstrip(b"\x00").decode("utf-8")


def _item_a_tupla(receta):
    """Convierte una Receta al formato necesario para struct.pack."""
    return (
        receta.id,
        _a_bytes(receta.nombre, 30),
        receta.tiempo_min,
        _a_bytes(receta.dificultad, 10),
        _a_bytes(receta.categoria, 15),
    )


def _tupla_a_item(datos):
    """Convierte un registro binario nuevamente a Receta."""
    return Receta(
        datos[0],
        _a_texto(datos[1]),
        datos[2],
        _a_texto(datos[3]),
        _a_texto(datos[4]),
    )


def guardar_binario(ruta, catalogo):
    """Guarda header y todos los registros del catálogo."""
    with open(ruta, "wb") as archivo:
        archivo.write(
            HEADER.pack(
                b"AYED",
                TEMA,
                catalogo.tamanio(),
            )
        )

        for receta in catalogo:
            archivo.write(
                FORMATO.pack(*_item_a_tupla(receta))
            )


def cargar_binario(ruta):
    """Carga y valida un catálogo binario."""
    try:
        archivo = open(ruta, "rb")
    except OSError as error:
        raise ArchivoInvalidoError(
            f"No se pudo abrir el archivo binario: {error}"
        )

    with archivo:
        cabecera = archivo.read(HEADER.size)

        if len(cabecera) != HEADER.size:
            raise ArchivoInvalidoError(
                "Binario truncado: header incompleto."
            )

        magia, tema, cantidad = HEADER.unpack(cabecera)

        if magia != b"AYED":
            raise ArchivoInvalidoError(
                "Magia incorrecta: el archivo no pertenece a este TP."
            )

        if tema != TEMA:
            raise ArchivoInvalidoError(
                "El archivo pertenece a otro tema."
            )

        catalogo = Recetario(cargar_catalogo=False)

        for _ in range(cantidad):
            datos = archivo.read(FORMATO.size)

            if len(datos) != FORMATO.size:
                raise ArchivoInvalidoError(
                    "Binario truncado: faltan registros."
                )

            receta = _tupla_a_item(
                FORMATO.unpack(datos)
            )
            catalogo.insertar_al_final(receta)

        return catalogo


def actualizar_registro(ruta, posicion, item):
    """
    Actualiza directamente un registro por posición.
    posicion es 0-based.
    """
    if posicion < 0:
        raise ArchivoInvalidoError(
            "La posición no puede ser negativa."
        )

    try:
        with open(ruta, "r+b") as archivo:
            archivo.seek(
                HEADER.size + posicion * FORMATO.size
            )

            datos = archivo.read(FORMATO.size)

            if len(datos) != FORMATO.size:
                raise ArchivoInvalidoError(
                    "La posición indicada no contiene un registro válido."
                )

            archivo.seek(
                HEADER.size + posicion * FORMATO.size
            )

            archivo.write(
                FORMATO.pack(*_item_a_tupla(item))
            )

    except OSError as error:
        raise ArchivoInvalidoError(
            f"No se pudo actualizar el archivo: {error}"
        )
