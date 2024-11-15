import random
def generarLista(tamaniolista,valorMinimo,valorMaximo,lista):  # no repite en mismo  numero 
    while tamaniolista != len(lista): #si se repite un numero, el tamaño de la lista no sera el mismo entonces ponemos la condicion que mientras en tamaño de la lista no sea el ingresado se seguira ejecuando el codigo
        numaleatorio= random.randint(valorMinimo,valorMaximo)
        if numaleatorio not in lista: # si el numero aleatorio no se repitio se guradara en la lista
            lista.append(numaleatorio)


def encontrarLista(num,lista):
    for i in range(len(lista)):
        if num== lista[i]:
            print(f"El numero encontrado esta en el indice:{i}") 
    return i 


