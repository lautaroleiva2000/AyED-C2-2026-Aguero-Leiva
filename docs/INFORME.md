# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Recetario
- Por qué lo eligieron (5–8 líneas): Elegimos el tema Recetario porque nos pareció una opción sencilla de comprender y cercana a situaciones cotidianas. Nos resultó interesante trabajar con recetas porque permite organizar información concreta como el nombre, el tiempo de preparación y la dificultad. También consideramos que es un tema fácil de explicar y de relacionar con los distintos contenidos que iremos viendo durante la materia. En esta primera entrega armamos manualmente un catálogo de recetas dentro del código. A partir de este catálogo podemos comenzar a trabajar con estructuras de datos y luego ir incorporando nuevas funcionalidades en las próximas entregas. Elegimos este tema porque creemos que nos va a permitir aplicar los conceptos de la materia de una forma clara y ordenada.
  
## 2. Modelo

En esta primera entrega, cada receta se representa mediante un diccionario con los datos: id, nombre, tiempo de preparación y dificultad.

El catálogo se guarda en una lista de Python, por lo que es una estructura mutable: se pueden agregar, eliminar o modificar elementos.

Cada receta se representa mediante un diccionario, que también es mutable. En cambio, los valores utilizados como el id (entero) y los textos de nombre y dificultad (cadenas) son tipos inmutables. Consideramos además que el id identifica de manera única a una receta y no debería cambiar una vez asignado.

## 3. Recursión (E2)

- **Función:** `desglosar_subrecetas(recetario, id_receta)`
- **Caso base:** Si la receta no contiene sub-recetas (es una receta o ingrediente hoja), devuelve `[id_receta]`.
- **Caso recursivo:** Si la receta tiene sub-recetas, devuelve `[id_receta] + desglosar_subrecetas(...)` para cada una de ellas.
- **Traza de un ejemplo real del dataset:**
  - **Datos del dataset:** La receta ID 10 (Empanadas de carne) utiliza la receta ID 3 (Sofrito) y la receta ID 5 (Masa de empanadas). Las recetas 3 y 5 no contienen sub-recetas.
  - **Llamada 1:** `desglosar_subrecetas(10)` $\rightarrow$ Tiene sub-recetas: [3, 5]. Llama recursivamente a 3 y luego a 5.
  - **Llamada 2:** `desglosar_subrecetas(3)` $\rightarrow$ NO tiene sub-recetas (**caso base**). Devuelve `[3]`.
  - **Llamada 3:** `desglosar_subrecetas(5)` $\rightarrow$ NO tiene sub-recetas (**caso base**). Devuelve `[5]`.
  - **Resultado final:** `[10, 3, 5]`

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
