def orden_burbuja(lista):
    n= len(lista)
    #recorre toda la lista
    for i in range(n):
        #ultimos i elementos ya estan ordenados 
        for j in range (0, n-1-1):
            #Intercambia si el elemento actaul es mayor al siguiente 

            if lista [j] > lista [j + 1]:
                lista [j], lista [j + 1] = lista [j + 1], lista[j]

    return lista 
#elemento de uso 
lista =[5,3,8,4,2,1]
print("Lista original:", lista)
lista_ordenada =orden_burbuja(lista)
print ("Lista ordenada:", lista_ordenada)


