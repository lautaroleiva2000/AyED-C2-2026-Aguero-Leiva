from src.dominio.libro_recetas import LibroRecetas
from src.dominio.menu_semanal import MenuSemanal
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.excepciones import (
    ColeccionLlenaError,
    PilaVaciaError,
    ColaVaciaError,
    ItemNoEncontradoError
)

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL: RECETARIO ---")
    print("1. Ver catálogo de recetas")
    print("2. Agregar receta al menú semanal (con tope)")
    print("3. Listar menú semanal")
    print("4. Deshacer última adición (Pila / Historial)")
    print("5. Atender/Cocinar siguiente en cola (Cola de preparación)")
    print("6. Ver desglose recursivo de receta")
    print("0. Salir")

def main():
    libro = LibroRecetas()
    menu_semanal = MenuSemanal(tope=6)
    pila_historial = Pila()
    cola_preparacion = Cola()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            print("¡Hasta luego!")
            break

        elif opcion == "1":
            print("\n--- CATÁLOGO DE RECETAS ---")
            for receta in libro:
                print(f"- {receta}")

        elif opcion == "2":
            nombre = input("Ingrese el nombre de la receta a agregar: ").strip()
            receta = libro.buscar(nombre)
            if receta:
                try:
                    menu_semanal.agregar(receta)
                    pila_historial.apilar(receta)
                    cola_preparacion.encolar(receta)
                    print(f"✓ Receta '{receta}' agregada con éxito al menú semanal.")
                except ColeccionLlenaError as e:
                    print(f"X Error: {e}")
            else:
                print("X No se encontró esa receta en el catálogo.")

        elif opcion == "3":
            print("\n--- MI MENÚ SEMANAL ---")
            if menu_semanal.esta_vacio():
                print("El menú semanal está vacío.")
            else:
                for receta in menu_semanal:
                    print(f"• {receta}")

        elif opcion == "4":
            try:
                receta_eliminada = pila_historial.desapilar()
                menu_semanal.eliminar(receta_eliminada)
                print(f"✓ Deshecho: Se eliminó '{receta_eliminada}' del menú semanal.")
            except PilaVaciaError as e:
                print(f"X Error: {e}")
            except ItemNoEncontradoError as e:
                print(f"X Error: {e}")

        elif opcion == "5":
            try:
                receta_a_cocinar = cola_preparacion.desencolar()
                print(f"✓ En preparación/Cocinando ahora: '{receta_a_cocinar}'")
            except ColaVaciaError as e:
                print(f"X Error: {e}")

        elif opcion == "6":
            nombre = input("Ingrese la receta para ver su desglose: ").strip()
            receta = libro.buscar(nombre)
            if receta and hasattr(receta, "desglosar"):
                print(receta.desglosar())
            else:
                print("X No se encontró la receta o no tiene desglose disponible.")

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
