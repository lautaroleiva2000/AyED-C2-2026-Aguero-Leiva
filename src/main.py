from pathlib import Path
from src.config import TEMA
from src.dominio.recetario import Recetario
from src.dominio.receta import Receta
from src.dominio.menu_semanal import MenuSemanal
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.persistencia.texto import cargar_texto, guardar_texto
from src.persistencia.binario import (
    guardar_binario,
    cargar_binario,
    actualizar_registro,
    alta_binario,
    baja_binario,
)
from src.excepciones import (
    ColeccionLlenaError,
    PilaVaciaError,
    ColaVaciaError,
    ItemNoEncontradoError,
    ArchivoInvalidoError,
)

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

RAIZ = Path(__file__).resolve().parents[1]
DATA = RAIZ / "data"
RUTA_TXT = DATA / "recetas.txt"
RUTA_BIN = DATA / "recetas.bin"
ENCABEZADOS = ["id", "nombre", "tiempo_min", "dificultad", "categoria"]

def filas_del_catalogo(catalogo):
    filas = []
    for r in catalogo:
        filas.append({
            "id": r.id,
            "nombre": r.nombre,
            "tiempo_min": r.tiempo_min,
            "dificultad": r.dificultad,
            "categoria": r.categoria,
        })
    return filas


def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal (menú semanal)")
    print("7. Historial (pila / deshacer)")
    print("8. Cola de preparación")
    print("9. Guardar / cargar archivos")
    print("0. Salir")


def gestionar_menu_semanal(recetario, menu_semanal, pila_historial, cola_preparacion):
    print("\n=== COLECCIÓN PRINCIPAL / MENÚ SEMANAL ===")
    print("1. Agregar receta al menú semanal")
    print("2. Listar menú semanal")
    print("3. Alta de receta en el catálogo")
    print("4. Modificar receta del catálogo")
    print("5. Eliminar receta del catálogo")
    print("0. Volver")

    opcion = input("> ").strip()

    if opcion == "1":
        nombre = input("Ingresá el nombre de la receta: ").strip()
        receta = recetario.buscar_por_nombre(nombre)

        if receta is None:
            print("Receta no encontrada.")
            return

        try:
            menu_semanal.agregar(receta)
            pila_historial.apilar(receta)
            cola_preparacion.encolar(receta)
            print(f"Receta agregada: {receta.nombre}")
        except ColeccionLlenaError as e:
            print(f"Error: {e}")

    elif opcion == "2":
        if menu_semanal.esta_vacio():
            print("El menú semanal está vacío.")
        else:
            for receta in menu_semanal:
                print(receta.resumen())

    elif opcion == "3":
        print("\n=== ALTA DE RECETA ===")

        id_texto = input("ID: ").strip()

        if not id_texto.isdigit():
            print("ID inválido.")
            return

        id_receta = int(id_texto)

        if recetario.buscar_receta(id_receta) is not None:
            print("Ya existe una receta con ese ID.")
            return

        nombre = input("Nombre: ").strip()
        tiempo_texto = input("Tiempo en minutos: ").strip()
        dificultad = input("Dificultad: ").strip()
        categoria = input("Categoría: ").strip()

        if not tiempo_texto.isdigit():
            print("Tiempo inválido.")
            return

        nueva_receta = Receta(
            id_receta,
            nombre,
            int(tiempo_texto),
            dificultad,
            categoria,
        )

        try:
            guardar_binario(RUTA_BIN, recetario)

            recetario.insertar_al_final(nueva_receta)
            alta_binario(RUTA_BIN, nueva_receta)

            guardar_texto(
                RUTA_TXT,
                filas_del_catalogo(recetario),
                ENCABEZADOS,
            )

            print("Receta agregada y guardada correctamente.")

        except ArchivoInvalidoError as error:
            print(f"Error de persistencia: {error}")

    elif opcion == "4":
        print("\n=== MODIFICAR RECETA ===")

        id_texto = input("ID de la receta a modificar: ").strip()

        if not id_texto.isdigit():
            print("ID inválido.")
            return

        id_receta = int(id_texto)
        receta = recetario.buscar_receta(id_receta)

        if receta is None:
            print("Receta no encontrada.")
            return

        posicion = recetario.posicion_del_id(id_receta)

        print(f"Receta actual: {receta.resumen()}")

        nombre = input("Nuevo nombre: ").strip()
        tiempo_texto = input("Nuevo tiempo en minutos: ").strip()
        dificultad = input("Nueva dificultad: ").strip()
        categoria = input("Nueva categoría: ").strip()

        if not tiempo_texto.isdigit():
            print("Tiempo inválido.")
            return

        try:
            guardar_binario(RUTA_BIN, recetario)

            receta.nombre = nombre
            receta.tiempo_min = int(tiempo_texto)
            receta.dificultad = dificultad
            receta.categoria = categoria

            actualizar_registro(
                RUTA_BIN,
                posicion,
                receta,
            )

            guardar_texto(
                RUTA_TXT,
                filas_del_catalogo(recetario),
                ENCABEZADOS,
            )

            print("Receta modificada y guardada correctamente.")

        except ArchivoInvalidoError as error:
            print(f"Error de persistencia: {error}")

    elif opcion == "5":
        print("\n=== ELIMINAR RECETA ===")

        id_texto = input("ID de la receta a eliminar: ").strip()

        if not id_texto.isdigit():
            print("ID inválido.")
            return

        id_receta = int(id_texto)
        receta = recetario.buscar_receta(id_receta)

        if receta is None:
            print("Receta no encontrada.")
            return

        posicion = recetario.posicion_del_id(id_receta)

        try:
            guardar_binario(RUTA_BIN, recetario)

            recetario.eliminar_receta(receta)
            baja_binario(RUTA_BIN, posicion)

            guardar_texto(
                RUTA_TXT,
                filas_del_catalogo(recetario),
                ENCABEZADOS,
            )

            print("Receta eliminada y cambios guardados correctamente.")

        except ArchivoInvalidoError as error:
            print(f"Error de persistencia: {error}")

    elif opcion != "0":
        print("Opción inválida.")

def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    try:
        filas = cargar_texto(RUTA_TXT)
        recetario = Recetario(cargar_catalogo=False)

        for fila in filas:
            receta = Receta(
                int(fila["id"]),
                fila["nombre"],
                int(fila["tiempo_min"]),
                fila["dificultad"],
                fila["categoria"],
            )
            recetario.insertar_al_final(receta)

    except ArchivoInvalidoError as error:
        print(f"No se pudo cargar el catálogo: {error}")
        recetario = Recetario()
    menu_semanal = MenuSemanal(tope=6)
    pila_historial = Pila()
    cola_preparacion = Cola()

    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()

        if opcion == "0":
            print("Chau.")

        elif opcion == "1":
            print("\n=== RECETARIO ===")
            recetario.listar_catalogo()

        elif opcion == "5":
            id_texto = input("Ingresá el ID de la receta: ").strip()

            if not id_texto.isdigit():
                print("ID inválido.")
            else:
                id_receta = int(id_texto)
                receta = recetario.buscar_receta(id_receta)

                if receta is None:
                    print("Receta no encontrada.")
                else:
                    resultado = recetario.desglosar_subrecetas(id_receta)
                    print(f"Desglose de {receta.nombre}: {resultado}")

        elif opcion == "6":
            gestionar_menu_semanal(
                recetario,
                menu_semanal,
                pila_historial,
                cola_preparacion,
            )

        elif opcion == "7":
            try:
                receta_eliminada = pila_historial.desapilar()
                menu_semanal.eliminar(receta_eliminada)
                print(f"Deshecho: se eliminó {receta_eliminada.nombre} del menú semanal.")
            except PilaVaciaError as e:
                print(f"Error: {e}")
            except ItemNoEncontradoError as e:
                print(f"Error: {e}")

        elif opcion == "8":
            try:
                receta_a_cocinar = cola_preparacion.desencolar()
                print(f"En preparación: {receta_a_cocinar.nombre}")
            except ColaVaciaError as e:
                print(f"Error: {e}")

        elif opcion == "3":
            print("\n=== BUSCAR RECETA ===")
            print("1. Búsqueda lineal")
            print("2. Búsqueda binaria")

            tipo_busqueda = input("> ").strip()
            nombre = input("Ingresá el nombre de la receta a buscar: ").strip().lower()

            if tipo_busqueda == "1":
                receta = busqueda_lineal(
                    recetario,
                    nombre,
                    lambda receta: receta.nombre.lower(),
                )

            elif tipo_busqueda == "2":
                recetas = list(recetario)

                print("Para usar búsqueda binaria, se ordenará primero el catálogo por nombre.")
                ordenar_insercion(
                    recetas,
                    lambda receta: receta.nombre.lower(),
                )

                receta = busqueda_binaria(
                    recetas,
                    nombre,
                    lambda receta: receta.nombre.lower(),
                )

            else:
                print("Opción inválida.")
                receta = None

            if tipo_busqueda in ("1", "2"):
                if receta is None:
                    print("Receta no encontrada.")
                else:
                    print("Receta encontrada:")
                    print(receta.resumen())

        elif opcion == "4":
            print("\n=== ORDENAR RECETARIO ===")
            print("1. Selección por nombre")
            print("2. Inserción por tiempo de preparación")

            opcion_orden = input("> ").strip()
            recetas = list(recetario)

            if opcion_orden == "1":
                ordenar_seleccion(recetas, lambda receta: receta.nombre.lower())
                print("\nRecetas ordenadas por nombre:")
                for receta in recetas:
                    print(receta.resumen())

            elif opcion_orden == "2":
                ordenar_insercion(recetas, lambda receta: receta.tiempo_min)
                print("\nRecetas ordenadas por tiempo:")
                for receta in recetas:
                    print(receta.resumen())

            else:
                print("Opción inválida.")
        
        elif opcion == "2":
            pendiente()

        elif opcion == "9":
            print("\n=== GESTIÓN DE ARCHIVOS ===")
            print("a) Cargar catálogo desde el .txt de la cátedra")
            print("b) Guardar catálogo en .txt")
            print("c) Guardar catálogo en binario (.bin)")
            print("d) Cargar catálogo desde binario (.bin)")
            sub = input("Subopción > ").strip().lower()
            try:
                if sub == "a":
                    filas = cargar_texto(RUTA_TXT)
                    recetario = Recetario(cargar_catalogo=False)
                    for fila in filas:
                        receta = Receta(
                            int(fila["id"]),
                            fila["nombre"],
                            int(fila["tiempo_min"]),
                            fila["dificultad"],
                            fila["categoria"],
                        )
                        recetario.insertar_al_final(receta)
                    print(f"Catálogo cargado desde .txt: {recetario.tamanio()} ítems.")
                elif sub == "b":
                    guardar_texto(RUTA_TXT, filas_del_catalogo(recetario), ENCABEZADOS)
                    print("Catálogo guardado en .txt.")
                elif sub == "c":
                    guardar_binario(RUTA_BIN, recetario)
                    print("Catálogo guardado en .bin.")
                elif sub == "d":
                    recetario = cargar_binario(RUTA_BIN)
                    print(f"Catálogo cargado desde .bin: {recetario.tamanio()} ítems.")
                else:
                    print("Subopción inválida.")
            except ArchivoInvalidoError as error:
                print(f"Archivo inválido: {error}")

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
