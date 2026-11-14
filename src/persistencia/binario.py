import struct
from pathlib import Path
from src.excepciones import ArchivoInvalidoError
from src.tads.lista_enlazada import ListaEnlazada
from src.dominio.recetario import Receta  # Ajustá el nombre de tu clase de dominio si es diferente

FORMATO = struct.Struct("<I 30s H 10s 15s")  # id, nombre(30), tiempo_min, dificultad(10), categoría(15) -> total bytes fijos
HEADER = struct.Struct("<4s 1s I")              # 9 bytes: magia, tema, cantidad
TEMA = b"R"                                   # R para Recetario

def _a_bytes(texto, ancho):
    """Texto -> bytes UTF-8 de 'ancho' exacto: recorta o rellena con \x00."""
    return texto.encode("utf-8")[:ancho].ljust(ancho, b"\x00")

def _a_texto(datos):
    """Bytes -> texto: le saca los \x00 del final."""
    return datos.rstrip(b"\x00").decode("utf-8")

def _item_a_tupla(r):
    """Objeto del dominio a tupla lista para FORMATO.pack."""
    return (
        r.id,
        _a_bytes(r.nombre, 30),
        r.tiempo_min,
        _a_bytes(r.dificultad, 10),
        _a_bytes(r.categoria, 15),
    )

def _tupla_a_item(t):
    """Tupla que salió de FORMATO.unpack a objeto del dominio."""
    return Receta(
        id=t[0],
        nombre=_a_texto(t[1]),
        tiempo_min=t[2],
        dificultad=_a_texto(t[3]),
        categoria=_a_texto(t[4]),
    )

def guardar_binario(ruta, catalogo):
    """Escribe el archivo completo: header (magia + tema + cantidad) + registros."""
    with open(ruta, "wb") as archivo:
        archivo.write(HEADER.pack(b"AYED", TEMA, catalogo.tamanio()))
        for item in catalogo:
            archivo.write(FORMATO.pack(*_item_a_tupla(item)))

def cargar_binario(ruta):
    """Lee el binario con validaciones. Devuelve la ListaEnlazada de ítems."""
    with open(ruta, "rb") as archivo:
        cabecera = archivo.read(HEADER.size)
        if len(cabecera) < HEADER.size:
            raise ArchivoInvalidoError("Binario truncado: ni siquiera tiene header completo.")
        magia, tema, cantidad = HEADER.unpack(cabecera)
        if magia != b"AYED":
            raise ArchivoInvalidoError("Magia incorrecta: este archivo no es de este TP.")
        if tema != TEMA:
            raise ArchivoInvalidoError(f"El tema del archivo ({tema!r}) no es el mío ({TEMA!r}).")
        
        catalogo = ListaEnlazada()
        for _ in range(cantidad):
            datos = archivo.read(FORMATO.size)
            if len(datos) < FORMATO.size:
                raise ArchivoInvalidoError("Binario truncado: el header dice más registros de los que hay.")
            catalogo.insertar_al_final(_tupla_a_item(FORMATO.unpack(datos)))
        return catalogo

def actualizar_registro(ruta, posicion, item):
    """Pisa SOLO el registro número 'posicion' (0-based) sin tocar el resto (Acceso Directo O(1))."""
    with open(ruta, "r+b") as archivo:
        archivo.seek(HEADER.size + posicion * FORMATO.size)
        archivo.write(FORMATO.pack(*_item_a_tupla(item)))