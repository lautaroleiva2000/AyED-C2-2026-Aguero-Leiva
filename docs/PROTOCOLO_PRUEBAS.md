# PROTOCOLO DE PRUEBAS

## Casos de Prueba - Entrega 3 (E3)

| ID | Área / Función | Acción realizada | Resultado esperado | Resultado obtenido | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **P05** | Colección con Tope | Agregar recetas hasta superar el límite de 6. | Debe lanzar `ColeccionLlenaError` y bloquear el ingreso de la 7ma receta. | Se captura la excepción y se muestra el mensaje de error correspondiente. | **PASA** |
| **P06** | Historial (Pila LIFO) | Intentar deshacer cuando el historial está vacío. | Debe lanzar `PilaVaciaError`. | Se captura la excepción en el menú y no rompe la ejecución. | **PASA** |
| **P07** | Cola de Espera (FIFO) | Intentar desatender/cocinar de la cola de preparación vacía. | Debe lanzar `ColaVaciaError`. | Se captura la excepción en el menú y muestra el mensaje indicativo. | **PASA** |
| **P08** | Iterador en Lista | Recorrer el catálogo y el menú semanal con bucle `for`. | Los elementos se muestran en el orden correcto utilizando `__iter__`. | Se recorre correctamente sin acceder a atributos privados de los nodos. | **PASA** |
