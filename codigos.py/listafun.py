import random

#def generarLista(tamaniolista,valorMinimo,valorMaximo,lista):
  #  for i in range(tamaniolista):
  #     numaleatorio= random.randint(valorMinimo,valorMaximo)
  #        lista.append(numaleatorio)
  #   return lista

def generarLista(tamaniolista,valorMinimo,valorMaximo,lista):
    while tamaniolista != len(lista):
        numaleatorio= random.randint(valorMinimo,valorMaximo)
        if numaleatorio not in lista:
            lista.append(numaleatorio)


def encontrarLista(num,lista):
    for i in range(len(lista)):
        if num== lista[i]:
            print(f"El numero encontrado esta en el indice:{i}") 
    return i 


