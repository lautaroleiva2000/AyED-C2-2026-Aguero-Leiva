def busqueda_lineal(coleccion, clave, obtener_clave):
    """Devuelve el ítem cuya clave coincide, o None."""
    for elemento in coleccion:
        if obtener_clave(elemento) == clave:
            return elemento

    return None


def busqueda_binaria(coleccion_ordenada, clave, obtener_clave):
    """La colección tiene que estar ordenada por obtener_clave."""
    izquierda = 0
    derecha = len(coleccion_ordenada) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor = obtener_clave(coleccion_ordenada[medio])

        if valor == clave:
            return coleccion_ordenada[medio]

        if valor < clave:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None
