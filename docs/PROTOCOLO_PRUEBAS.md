# Protocolo de pruebas

Pruebas manuales. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | dataset inicial | lista no vacía, sin traceback | pasa | Prueba de regresión de E1 |
| P02 | E1 | Buscar un ítem inexistente | id = -1 | mensaje claro, el menú sigue | no corrido | Prueba de regresión |
| P03 | E2 | Operación recursiva sobre receta CON sub-recetas | id = 10 (Empanadas de carne) | devuelve la cadena completa `[10, 3, 5]` | pasa | Prueba de regresión de E2 |
| P04 | E2 | Operación recursiva sobre receta SIN sub-recetas | id = 3 (Sofrito) | devuelve solamente `[3]` (caso base) | pasa | Prueba de regresión de E2 |
| P05 | E3 | Agregar recetas a la colección principal hasta superar el tope | menú semanal con tope = 6 | al intentar agregar la 7ma receta lanza `ColeccionLlenaError` y no supera el límite | pasa | Colección principal sobre `ListaEnlazada` |
| P06 | E3 | Intentar deshacer cuando el historial está vacío | pila vacía | lanza `PilaVaciaError`, el menú captura la excepción y continúa funcionando | pasa | Pila LIFO sobre `ListaEnlazada` |
| P07 | E3 | Intentar cocinar/desencolar con la cola de preparación vacía | cola vacía | lanza `ColaVaciaError`, el menú captura la excepción y continúa funcionando | pasa | Cola FIFO sobre `ListaEnlazada` |
| P08 | E3 | Recorrer el catálogo y el menú semanal mediante `for` | recetas cargadas | los elementos aparecen en el orden correcto usando el iterador, sin acceder directamente a `_cabeza` | pasa | Verificar `__iter__` |
| P09 | E4 | Búsqueda lineal de un nombre que existe | | lo encuentra | no corrido | |
| P10 | E4 | Búsqueda lineal de un nombre que no existe | | no encontrado, sin traceback | no corrido | |
| P11 | E4 | Búsqueda binaria con catálogo desordenado | | avisa o reordena; no da un falso hit | no corrido | |
| P12 | E4 | Ordenar por un criterio y después por otro | | el orden cambia | no corrido | |
| P13 | E5 | Guardar CSV, salir, volver a entrar | | los datos siguen | no corrido | |
| P14 | E5 | Guardar binario y modificar un registro por id | | al recargar, ese campo cambió | no corrido | |
| P15 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido | no corrido | |
