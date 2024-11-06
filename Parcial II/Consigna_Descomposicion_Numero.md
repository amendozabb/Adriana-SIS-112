
# Consigna: Descomposición Recursiva de un Número en Dígitos

**Objetivo:**  
Implementar una función en Python que descomponga un número entero en una lista de sus dígitos utilizando recursión.

## Instrucciones:

1. **Crear la función `descomponer_numero`**:
   - La función debe recibir como parámetro un número entero `n`.
   - La función debe devolver una lista en la que cada elemento es un dígito del número `n`, en el mismo orden en que aparecen.

2. **Consideraciones del problema**:
   - Define un **caso base**: Cuando `n` sea menor que 10, la función debe devolver `[n]` como lista con un solo elemento.
   - Para el **caso recursivo**, la función debe llamar a sí misma con el valor de `n` dividido entre 10 (para eliminar el último dígito), y luego agregar el último dígito de `n` (obtenido con `n % 10`) al final de la lista.
   - **Ejemplo** de comportamiento esperado:
     ```python
     descomponer_numero(32345)  # Retorna [3, 2, 3, 4, 5]
     ```

3. **Ejemplos de prueba**:

     - `descomponer_numero(105)`: Debe retornar `[1, 0, 5]`.
     - `descomponer_numero(7)`: Debe retornar `[7]`.
     - `descomponer_numero(50003)`: Debe retornar `[5, 0, 0, 0, 3]`.

