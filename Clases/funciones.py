vector = []
def menu():
    print("NOTAS TRIMESTRE II GESTION 2024")
    print("ACCESO SOLO A DOCENTES!")
    print("1. Agregar nota")
    print("2. Eliminar nota")
    print("3. Modificar nota")
    print("4. Mostrar todas las notas")
    print("5. Calcular promedio")
    print("6. Nota maxima y minima")

def agregar(nota):
    if (nota<=100) and (nota>0):
        vector.append(nota)
    else:
        print("Nota invalida")
        
def eliminar(nota):
    
    nota=nota-1
    vector.pop(nota)

def modificar(indice, nota):
    indice-=1
    vector[indice] = nota
    
def mostrar():
    print(vector)
    
def promedio():
    lectura= len(vector)
    promedio=0
    for i in range(len(vector)):
        promedio=promedio + vector[i-1]
    final= promedio/lectura
    print(f"El promedio de todas las notas es {final}")

def maxmin():
    print(f"La nota maxima es {max(vector)} y la nota minima es {min(vector)}")