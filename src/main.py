from src.config import TEMA
from src.dominio.recetario import Recetario

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
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return
        
    recetario = Recetario()

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

        elif opcion in ("2", "3", "4", "6", "7", "8", "9"):
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
