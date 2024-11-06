
# Actividad de Programación: Creación de un Menú en Python

## Objetivo
Desarrollar un programa en Python que permita a los usuarios:
- Crear listas con datos únicos (de forma manual o generados aleatoriamente).
- Aplicar métodos de búsqueda (búsqueda lineal y búsqueda binaria).
- Ordenar la lista para aplicar la búsqueda binaria.
- Trabajar en dos archivos separados.

## Instrucciones
1. **Organización de Archivos**:
   - Divide el código en dos archivos Python:
     - `main.py`: donde estará el menú principal con las opciones.
     - `funciones.py`: donde estarán las funciones que realizarán las operaciones de la lista.

2. **Estructura del Menú**
   - El archivo `menu_principal.py` debe tener un menú con las siguientes opciones:
     1. **Generar una lista única de números ingresados por teclado.**
        - Permitir que el usuario ingrese los elementos de la lista manualmente, verificando que no se repitan.
     2. **Generar una lista de `n` números aleatorios únicos.**
        - Pedir al usuario el tamaño `n` de la lista y generar números aleatorios sin repetir.
     3. **Ordenar la lista.**
        - Implementa un método de ordenamiento (por ejemplo, burbuja o selección) para ordenar la lista actual. (preguntar al usuario que lista ordenar la que se genero ingresando datos por teclado o la generada aleatoriamente)
     4. **Búsqueda Lineal.**
        - Permitir que el usuario ingrese un número y buscarlo en la lista utilizando el método de búsqueda lineal.(debe haber un menu que permita al usuario elegir que lista usar, la que se genero ingresando datos por teclado o la generada aleatoriamente)

     5. **Búsqueda Binaria.**
        - Antes de realizar la búsqueda binaria, mostrar un mensaje que recuerde al usuario que la lista debe estar ordenada para este tipo de búsqueda.
        - Realizar la búsqueda binaria solo si el usuario ha confirmado que la lista está ordenada. (debe haber un menu que permita al usuario elegir que lista usar, la que se genero ingresando datos por teclado o la generada aleatoriamente)
     6. **Salir.**
        - Salir del programa.

3. **Desarrollo de Funciones**
   - En el archivo `funciones.py`, implementa las siguientes funciones:
     - **`ingresar_lista()`**: Permite al usuario ingresar números por teclado, asegurando que no se repitan en la lista.
     - **`generar_lista_aleatoria(n)`**: Genera una lista de `n` números aleatorios únicos.
     - **`ordenar_lista(lista)`**: Ordena la lista utilizando un método de ordenamiento.
     - **`busqueda_lineal(lista, numero)`**: Realiza la búsqueda lineal de un número en la lista.
     - **`busqueda_binaria(lista, numero)`**: Realiza la búsqueda binaria en la lista **ordenada**.

4. **Validaciones y Mensajes**
   - En la opción de **Búsqueda Binaria**, verifica que el usuario sea consciente de que la lista debe estar ordenada. Muestra un mensaje recordando esto y permite que el usuario decida si la lista está ordenada o si prefiere ordenarla antes.

5. **Ejemplo de Ejecución del Menú**
   ```plaintext
   Menú Principal
   1. Ingresar lista manualmente
   2. Generar lista aleatoria
   3. Ordenar lista
   4. Búsqueda lineal
   5. Búsqueda binaria
   6. Salir
   ```

6. **Consejos**:
   - Se debe crear dos listas, una para que el usuario la cree con la opcion 1 y otra aleatoria, para luego en los puntos que sea necesario preguntar al usuario que lista usar
   - Usa la biblioteca `random` para generar números aleatorios.
   - Para verificar la unicidad en las listas, considera el uso de estructuras como conjuntos (`set`).
   - Utiliza bucles y estructuras de control para validar las entradas del usuario.

7. **Ejemplo de Salida**:
   - Al realizar una búsqueda, muestra la posición del número en la lista o un mensaje indicando que el número no fue encontrado.
   - Al ordenar, muestra la lista antes y después de ordenar para que el usuario vea el cambio.

### Recursos Sugeridos
- Biblioteca `random` para generar números aleatorios.
- Funciones `input()` para recibir datos del usuario y `print()` para mostrar resultados.

---

Con esta actividad, los estudiantes aprenderán a estructurar el código en varios archivos, implementar menús interactivos y aplicar métodos de búsqueda y ordenamiento en listas.
