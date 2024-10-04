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
    

     

