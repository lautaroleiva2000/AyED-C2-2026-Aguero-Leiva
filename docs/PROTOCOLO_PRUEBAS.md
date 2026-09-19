# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | dataset inicial | lista no vacía, sin traceback | no corrido | |
| P02 | E1 | Buscar un ítem inexistente | id = -1 | mensaje claro, el menú sigue | no corrido | |
| P03 | E2 | Operación recursiva sobre receta CON sub-recetas | id = 10 (Empanadas) | imprime la cadena completa de sub-recetas | no corrido | |
| P04 | E2 | Operación recursiva sobre receta SIN sub-recetas | id = 3 (Sofrito) | solo el ítem (caso base) | no corrido | |
| P05 | E2 | Ver el detalle de una receta existente | id = 1 | muestra todos los datos de la receta | no corrido | |
| P06 | E2 | Ver el detalle de una receta inexistente | id = 999 | mensaje de advertencia sin cortar el menú | no corrido | |
| P07 | E2 | Elegir opción de menú inválida | opción "9z" | mensaje de opción inválida y re-despliega menú | no corrido | |
| P08 | E2 | Ingresar Enter vacío en el menú | texto vacío | no falla y vuelve a solicitar opción | no corrido | |
| P09 | E4 | Búsqueda lineal de un nombre que existe | | lo encuentra | no corrido | |
| P10 | E4 | Búsqueda lineal de un nombre que no existe | | no encontrado, sin traceback | no corrido | |
| P11 | E4 | Búsqueda binaria con catálogo desordenado | | avisa o reordena; no da un falso hit | no corrido | |
| P12 | E4 | Ordenar por un criterio y después por otro | | el orden cambia | no corrido | |
| P13 | E5 | Guardar CSV, salir, volver a entrar | | los datos siguen | no corrido | |
| P14 | E5 | Guardar binario y modificar un registro por id | | al recargar, ese campo cambió | no corrido | |
| P15 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido | no corrido | |
