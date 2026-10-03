## 4. Estructuras de Datos (TADs Lineales - Entrega 3)

### Tabla de Operaciones e Invariantes

| TAD | Operación | Descripción | Complejidad | Invariante de Estructura |
| :--- | :--- | :--- | :--- | :--- |
| **ListaEnlazada** | `insertar_al_inicio(dato)` | Inserta un nuevo nodo al inicio de la lista. | O(1) | `self._tamanio` refleja el conteo exacto de nodos. |
| **ListaEnlazada** | `insertar_al_final(dato)` | Recorre la lista y agrega un nodo al final. | O(n) | El último nodo siempre apunta a `None`. |
| **ListaEnlazada** | `eliminar(dato)` | Remueve el nodo con el dato especificado. | O(n) | La cadena de enlaces se mantiene intacta. |
| **Pila** | `apilar(dato)` / `desapilar()` | Comportamiento LIFO. Insertar y extraer por la cabeza. | O(1) | El elemento extraído es siempre el último ingresado. |
| **Cola** | `encolar(dato)` / `desencolar()` | Comportamiento FIFO. Inserta al final y saca por cabeza. | O(1) desencolar / O(n) encolar | Se respeta el orden de llegada de los elementos. |
| **MenuSemanal** | `agregar(receta)` | Colección principal con tope máximo (6 elementos). | O(n) | `tamanio() <= 6`. Si se supera, lanza `ColeccionLlenaError`. |
