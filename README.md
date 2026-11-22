# AyED C2 2026 — Recetario — Grupo 51

## Integrantes

| Nombre | Mail | GitHub |
| --- | --- | --- |
| Luciana Agüero | luciana.ailen.aguero@gmail.com | @agueroluciana |
| Lautaro Leiva | lautaroleiva2000@gmail.com | @lautaroleiva2000 |

## Tema

Recetario por consola desarrollado como trabajo integrador de Algoritmos y Estructuras de Datos.

El programa permite administrar un catálogo de recetas y trabajar con distintas estructuras y algoritmos vistos durante la materia.

## Cómo ejecutar

Requiere Python 3.10 o superior.

Desde la raíz del repositorio:

```text
python -m src.main
```

En Windows, si `python` no funciona:

```text
py -3 -m src.main
```

El proyecto utiliza únicamente la biblioteca estándar de Python.

## Qué hace

El programa incluye las siguientes operaciones:

1. Listar el catálogo de recetas.
2. Ver el detalle de una receta por ID.
3. Buscar recetas mediante búsqueda lineal o binaria.
4. Ordenar recetas por nombre o tiempo de preparación utilizando algoritmos propios.
5. Realizar un desglose recursivo de sub-recetas.
6. Administrar un menú semanal con un máximo de 6 recetas y realizar altas, modificaciones y bajas persistentes.
7. Utilizar una pila como historial para deshacer la última receta agregada al menú semanal.
8. Utilizar una cola para administrar el orden de preparación de las recetas.
9. Guardar y cargar el catálogo en archivos de texto y binarios.
10. Salir del programa de forma controlada.

## Estructuras y algoritmos utilizados

- Lista enlazada.
- Pila.
- Cola.
- Recursión.
- Búsqueda lineal.
- Búsqueda binaria.
- Ordenamiento por selección.
- Ordenamiento por inserción.
- Persistencia en texto.
- Persistencia binaria con `struct`.
- Actualización de registros por posición mediante `seek`.

## Persistencia

El catálogo principal se carga desde:

```text
data/recetas.txt
```

El programa también puede generar un archivo binario:

```text
data/recetas.bin
```

Los archivos `.bin` generados durante la ejecución no se incluyen en el repositorio.

## Limitaciones conocidas

- El menú semanal tiene un máximo de 6 recetas.
- La pila de historial y la cola de preparación son estructuras independientes.
- Al deshacer una receta desde la pila, la receta se elimina del menú semanal, pero no se elimina automáticamente de la cola de preparación.
- La búsqueda binaria requiere una colección ordenada; por ese motivo el programa ordena previamente una copia del catálogo por nombre.

## Documentación

Dentro de la carpeta `docs/` se encuentran:

- `INFORME.md`
- `PROTOCOLO_PRUEBAS.md`
- `DECLARACION_IA.md`

Estos archivos documentan el desarrollo de las distintas entregas, las pruebas realizadas y el uso de herramientas de inteligencia artificial.
