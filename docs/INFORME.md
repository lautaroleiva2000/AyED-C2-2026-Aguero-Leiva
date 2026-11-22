# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- **Integrantes:** Luciana Agüero y Lautaro Leiva.
- **Tema:** Recetario.
- **Por qué lo eligieron:** Elegimos el tema Recetario porque nos pareció una opción sencilla de comprender y cercana a situaciones cotidianas. Nos resulta interesante trabajar con recetas porque permite organizar información concreta como el nombre, el tiempo de preparación y la dificultad. También consideramos que es un tema fácil de explicar y de relacionar con los distintos contenidos que iremos viendo durante la materia. En la primera entrega armamos manualmente un catálogo de recetas dentro del código. A partir de este catálogo fuimos incorporando nuevas funcionalidades y estructuras de datos en las entregas siguientes. Elegimos este tema porque creemos que nos permite aplicar los conceptos de la materia de una forma clara y ordenada.

## 2. Modelo

Cada receta se representa mediante un objeto de la clase `Receta`. Sus atributos son:

- `id`
- `nombre`
- `tiempo_min`
- `dificultad`
- `categoria`

El `id` identifica de forma única a cada receta y no debería modificarse una vez asignado. En cambio, el nombre, el tiempo de preparación, la dificultad y la categoría son datos mutables, ya que el programa permite modificarlos mediante el ABM del catálogo.

El `Recetario` representa el catálogo general de recetas. Internamente almacena los objetos `Receta` en una `ListaEnlazada` propia. También mantiene las relaciones entre algunas recetas para realizar el desglose recursivo. Por ejemplo, la receta 10, Empanadas de carne, se relaciona con las recetas 3, Sofrito, y 5, Masa de empanadas.

El `MenuSemanal` representa la colección principal del programa. También utiliza una `ListaEnlazada`, pero tiene un tope máximo de 6 recetas. Las recetas seleccionadas desde el catálogo pueden incorporarse a este menú.

Cuando se agrega una receta al menú semanal, el mismo objeto también se incorpora a dos estructuras auxiliares:

- La `Pila` representa el historial de incorporaciones y permite deshacer utilizando comportamiento LIFO: la última receta agregada es la primera en salir.
- La `Cola` representa el orden de preparación y utiliza comportamiento FIFO: la primera receta agregada es la primera en salir.

De esta manera, el catálogo, el menú semanal, la pila y la cola cumplen responsabilidades diferentes, pero trabajan con objetos `Receta` del mismo dominio.

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

| TAD | Operación | Descripción | Complejidad | Invariante | Dónde se usa |
|---|---|---|---|---|---|
| **ListaEnlazada** | `insertar_al_inicio(dato)` | Inserta un nuevo nodo al inicio de la lista. | O(1) | `self._tamanio` refleja el número exacto de nodos. | Es la estructura base utilizada internamente por el Recetario, el MenuSemanal, la Pila y la Cola. |
| **ListaEnlazada** | `insertar_al_final(dato)` | Recorre la lista y agrega un nodo al final. | O(n) | El último nodo siempre apunta a `None`. | Se utiliza para almacenar las recetas del catálogo, agregar recetas al menú semanal y encolar elementos. |
| **ListaEnlazada** | `eliminar(dato)` | Busca y elimina el nodo que contiene el dato indicado. | O(n) | Después de eliminar un nodo, la cadena de enlaces continúa siendo válida. | Se utiliza al eliminar recetas y también como operación interna de la pila y la cola. |
| **Pila** | `apilar(dato)` / `desapilar()` | Implementa comportamiento LIFO: el último elemento ingresado es el primero que sale. | O(1) | El tope representa siempre el último elemento incorporado. | Se utiliza como historial para deshacer la última receta agregada al menú semanal mediante la opción 7. |
| **Cola** | `encolar(dato)` / `desencolar()` | Implementa comportamiento FIFO: el primer elemento ingresado es el primero que sale. | O(n) encolar / O(1) desencolar | Se mantiene el orden de llegada de los elementos. | Se utiliza como cola de preparación de recetas mediante la opción 8. |
| **MenuSemanal** | `agregar(receta)` / `eliminar(receta)` | Colección principal del dominio con un máximo de 6 recetas. | O(n) | Su tamaño nunca puede superar el tope de 6 recetas. Si se intenta superarlo, lanza `ColeccionLlenaError`. | Se utiliza en la opción 6 para armar y administrar el menú semanal. |

La `ListaEnlazada` funciona como estructura base para varios componentes del programa. La `Pila` y la `Cola` reutilizan esta estructura, pero ofrecen comportamientos diferentes: LIFO para el historial y FIFO para el orden de preparación.

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

## 6. Persistencia (Entrega 5)

En la Entrega 5 se incorporó persistencia del catálogo tanto en formato de texto simple (`.txt`) como en formato binario (`.bin`). El catálogo se carga desde `data/recetas.txt` al iniciar el programa, permitiendo conservar los cambios realizados entre distintas ejecuciones.

El archivo de texto utiliza los campos:

`id,nombre,tiempo_min,dificultad,categoria`

Para la persistencia binaria se utiliza `struct` con registros de longitud fija.

- **Formato del registro:** `struct.Struct("<I 30s H 10s 15s")`
- **Tamaño de cada registro:** 61 bytes.
- **Campos:**
  - `id`: entero sin signo de 4 bytes.
  - `nombre`: cadena de 30 bytes.
  - `tiempo_min`: entero sin signo de 2 bytes.
  - `dificultad`: cadena de 10 bytes.
  - `categoria`: cadena de 15 bytes.

El archivo binario comienza con un encabezado:

- **Formato del header:** `struct.Struct("<4s 1s I")`
- **Tamaño:** 9 bytes.
- **Magia:** `AYED`.
- **Tema:** `R`, correspondiente a Recetario.
- **Cantidad:** número de registros almacenados.

La modificación de un registro existente se realiza mediante acceso directo utilizando:

`seek(HEADER.size + posicion * FORMATO.size)`

De esta manera se accede directamente a la posición del registro y se sobrescribe únicamente ese registro.

El alta agrega un nuevo registro al final del archivo binario y actualiza la cantidad almacenada en el encabezado. La baja elimina el registro correspondiente y reescribe el archivo, ya que los registros posteriores deben desplazarse para evitar dejar un espacio vacío.

También se implementó manejo de `ArchivoInvalidoError` para archivos truncados, archivos con una magia incorrecta y archivos de texto con una cantidad inválida de campos. En estos casos el programa muestra un mensaje claro y continúa funcionando sin finalizar con un traceback.

Se realizaron las pruebas P13, P14 y P15. Se verificó la persistencia de altas y modificaciones después de cerrar y volver a ejecutar el programa, la actualización directa de un registro binario por posición y el manejo controlado de archivos inválidos.

## 7. Reparto de trabajo

El trabajo se realizó de manera grupal entre Luciana Agüero y Lautaro Leiva. A lo largo de las distintas entregas se fueron repartiendo tareas de implementación, revisión, pruebas, documentación e integración del proyecto.

- **Luciana Agüero:** participó principalmente en la implementación inicial de distintas partes del programa, incluyendo estructuras de datos y funciones desarrolladas durante las entregas. También trabajó sobre partes de la persistencia de archivos y colaboró con la documentación del proyecto.

- **Lautaro Leiva:** trabajó principalmente en la revisión e integración del código entre las distintas entregas, corrección de errores, ejecución de pruebas manuales, actualización de la documentación y organización del repositorio y las entregas en GitHub.

Aunque hubo una división de tareas, ambos integrantes revisaron el funcionamiento general del Recetario y conocen la estructura del programa. Los dos pueden explicar el funcionamiento del catálogo, la colección principal, la recursión, la lista enlazada, la pila, la cola, los algoritmos de búsqueda y ordenamiento y la persistencia en texto y binario.
