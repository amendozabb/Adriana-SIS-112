import random

def generarLista(tamaniolista,valorMinimo,valorMaximo,lista):
    for i in range(tamaniolista):
        numaleatorio= random.randint(valorMinimo,valorMaximo)
        lista.append(numaleatorio)
    return lista

def encontrarLista(num,lista):
    for i in range(len(lista)):
        if num== lista[i]:
            print(f"El numero encontrado esta en el indice:{i}") 
    
def busqueda_binaria(lista, numero):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == numero:
            return medio
        elif lista[medio] < numero:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
     

