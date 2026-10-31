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

## 5. Complejidad y Mediciones (Entrega 4)

### 1. Tabla de Complejidad de las Operaciones

| Operación | Tiempo | Espacio | Por qué |
| :--- | :--- | :--- | :--- |
| Listar catálogo | O(n) | O(1) | Recorre los n elementos una vez mediante el iterador. |
| Búsqueda lineal | O(n) | O(1) | En el peor caso debe revisar todos los elementos hasta encontrar la receta o llegar al final. |
| Búsqueda binaria | O(log n) | O(1) | En cada comparación descarta aproximadamente la mitad del rango de búsqueda. Requiere que la colección esté previamente ordenada. |
| Ordenar por selección | O(n²) | O(1) | Utiliza dos recorridos anidados para buscar el menor elemento de cada parte de la colección. |
| Ordenar por inserción | O(n) mejor / O(n²) peor | O(1) | Si la colección ya está ordenada realiza pocas comparaciones; en el peor caso debe desplazar muchos elementos por cada inserción. |

En el caso de la búsqueda binaria utilizada desde el menú, el catálogo se convierte primero desde `ListaEnlazada` a una lista de Python y se ordena mediante nuestro algoritmo de inserción. La complejidad O(log n) corresponde específicamente al algoritmo de búsqueda binaria una vez que la colección ya está ordenada.

### 2. Mediciones reales con `time.perf_counter()`

Se realizaron mediciones sobre el catálogo original de 5 recetas y sobre una copia agrandada 100 veces, con 500 elementos. Para reducir el efecto de variaciones muy pequeñas de tiempo, cada operación se ejecutó repetidas veces y se tomó un tiempo promedio.

Para la búsqueda lineal se utilizó una receta inexistente, obligando al algoritmo a recorrer toda la colección. Para la búsqueda binaria se midió solamente la búsqueda sobre una colección previamente ordenada.

| Operación | n = 5 | n = 500 |
| :--- | ---: | ---: |
| Búsqueda lineal | 0.000000857 s | 0.000049815 s |
| Búsqueda binaria | 0.000000780 s | 0.000001980 s |
| Ordenamiento por selección | 0.000003657 s | 0.023023703 s |
| Ordenamiento por inserción | 0.000001173 s | 0.007645837 s |

### 3. Conclusión de las mediciones

Al aumentar el tamaño del dataset de 5 a 500 elementos, la búsqueda lineal aumenta claramente su tiempo porque puede necesitar recorrer toda la colección. En cambio, la búsqueda binaria presenta un aumento mucho menor porque en cada paso descarta aproximadamente la mitad de los elementos.

Los ordenamientos por selección e inserción muestran un crecimiento mucho mayor al aumentar el tamaño de la entrada, consistente con su comportamiento cuadrático en el peor caso. Las mediciones reales pueden variar según el equipo y la ejecución, pero permiten observar la diferencia entre los distintos órdenes de complejidad.
