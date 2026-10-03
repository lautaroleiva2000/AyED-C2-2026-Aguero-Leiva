# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- **Tema:** Recetario
- **Por qué lo eligieron:** Elegimos el tema Recetario porque nos pareció una opción sencilla de comprender y cercana a situaciones cotidianas. Nos resulta interesante trabajar con recetas porque permite organizar información concreta como el nombre, el tiempo de preparación y la dificultad. También consideramos que es un tema fácil de explicar y de relacionar con los distintos contenidos que iremos viendo durante la materia. En la primera entrega armamos manualmente un catálogo de recetas dentro del código. A partir de este catálogo fuimos incorporando nuevas funcionalidades y estructuras de datos en las entregas siguientes. Elegimos este tema porque creemos que nos permite aplicar los conceptos de la materia de una forma clara y ordenada.

## 2. Modelo

Cada receta se representa mediante un objeto de la clase `Receta`, con los datos: id, nombre, tiempo de preparación y dificultad.

En la primera entrega el catálogo se había armado utilizando una lista de Python. A partir de la Entrega 3, el catálogo del `Recetario` utiliza una `ListaEnlazada` propia, implementada mediante nodos y referencias al siguiente elemento.

El identificador `id` permite distinguir de manera única cada receta y no debería modificarse una vez asignado.

Las relaciones entre recetas se utilizan para representar las sub-recetas necesarias para el desglose recursivo implementado en la Entrega 2.

## 3. Recursión (E2)

- **Función:** `Recetario.desglosar_subrecetas(self, id_receta)`
- **Caso base:** Si la receta no contiene sub-recetas (es una receta o ingrediente hoja), devuelve `[id_receta]`.
- **Caso recursivo:** Si la receta tiene sub-recetas, comienza con `[id_receta]` y agrega el resultado de `desglosar_subrecetas(...)` para cada una de ellas.
- **Traza de un ejemplo real del dataset:**
  - **Datos del dataset:** La receta ID 10 (Empanadas de carne) utiliza la receta ID 3 (Sofrito) y la receta ID 5 (Masa de empanadas). Las recetas 3 y 5 no contienen sub-recetas.
  - **Llamada 1:** `desglosar_subrecetas(10)` → Tiene sub-recetas `[3, 5]`. Llama recursivamente a 3 y luego a 5.
  - **Llamada 2:** `desglosar_subrecetas(3)` → No tiene sub-recetas (**caso base**). Devuelve `[3]`.
  - **Llamada 3:** `desglosar_subrecetas(5)` → No tiene sub-recetas (**caso base**). Devuelve `[5]`.
  - **Retorno de las llamadas:**
    - La receta 3 devuelve `[3]`. El resultado acumulado pasa a ser `[10, 3]`.
    - La receta 5 devuelve `[5]`. El resultado acumulado pasa a ser `[10, 3, 5]`.
    - La llamada inicial termina y devuelve `[10, 3, 5]`.
- **Resultado final:** `[10, 3, 5]`

## 4. Estructuras de Datos (TADs Lineales - Entrega 3)

### Tabla de Operaciones e Invariantes

| TAD | Operación | Descripción | Complejidad | Invariante de Estructura |
|---|---|---|---|---|
| **ListaEnlazada** | `insertar_al_inicio(dato)` | Inserta un nuevo nodo al inicio de la lista. | O(1) | `self._tamanio` refleja el conteo exacto de nodos. |
| **ListaEnlazada** | `insertar_al_final(dato)` | Recorre la lista y agrega un nodo al final. | O(n) | El último nodo siempre apunta a `None`. |
| **ListaEnlazada** | `eliminar(dato)` | Remueve el nodo con el dato especificado. | O(n) | La cadena de enlaces se mantiene intacta. |
| **Pila** | `apilar(dato)` / `desapilar()` | Comportamiento LIFO. Insertar y extraer por la cabeza. | O(1) | El elemento extraído es siempre el último ingresado. |
| **Cola** | `encolar(dato)` / `desencolar()` | Comportamiento FIFO. Inserta al final y saca por cabeza. | O(1) desencolar / O(n) encolar | Se respeta el orden de llegada de los elementos. |
| **MenuSemanal** | `agregar(receta)` | Colección principal con tope máximo (6 elementos). | O(n) | `tamanio() <= 6`. Si se supera, lanza `ColeccionLlenaError`. |
