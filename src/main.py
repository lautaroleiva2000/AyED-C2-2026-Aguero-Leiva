from src.config import TEMA
from src.dominio.recetario import Recetario
from src.dominio.menu_semanal import MenuSemanal
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.excepciones import (
    ColeccionLlenaError,
    PilaVaciaError,
    ColaVaciaError,
    ItemNoEncontradoError,
)

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}


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
    print("\n=== MENÚ SEMANAL ===")
    print("1. Agregar receta")
    print("2. Listar menú semanal")
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

    elif opcion != "0":
        print("Opción inválida.")


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

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

        elif opcion in ("2", "3", "4", "9"):
            pendiente()

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
