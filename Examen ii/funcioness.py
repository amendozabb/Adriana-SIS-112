import random

def lista_personalizada(tamanio, listaP):
    tamanio= int(input("Ingrese el numero de digitos de la lista"))
    for i in range(tamanio):
        n=("Ingrese el numero")
        listaP.append(n)
    return listaP   

def lista_aleatoria(tamaniolista,lista):  # no repite en mismo  numero 
    while tamaniolista != len(lista): #si se repite un numero, el tamaño de la lista no sera el mismo entonces ponemos la condicion que mientras en tamaño de la lista no sea el ingresado se seguira ejecuando el codigo
        numaleatorio= random.randint(0,tamaniolista)
        if numaleatorio not in lista: # si el numero aleatorio no se repitio se guradara en la lista
            lista.append(numaleatorio)

def orden_burbuja(lista):
    n= len(lista)
    #recorre toda la lista
    for i in range(n):
        #ultimos i elementos ya estan ordenados 
        for j in range (0, n-1-1):
            #Intercambia si el elemento actaul es mayor al siguiente 

            if lista [j] > lista [j + 1]:
                lista [j], lista [j + 1] = lista [j + 1], lista[j]

def busqueda_lineal(num,lis): #encontar un numero
    for i in range(len(lis)): #se repite el bucle n veces(tamaño de la lista) 
        if num== lis[i]: #se compara
            print(f"El numero encontrado esta en el indice:{i}") 
    return i 

def busqueda_binaria(lista, num):
    lista_ordenada= orden_burbuja(lista)
    fin =len(lista_ordenada) - 1
    inicio= 0 
    while inicio <= fin:
        medio =(inicio+ fin) // 2
        print ("=========\n indice del medio:",medio,"\n Valor:",lista_ordenada[medio])
        if lista[medio]== num:
           return medio
        elif num >lista_ordenada[medio]:
            inicio=medio +1
        else:
            fin= medio -1
    return -1

def descomponer_numero(n):
    # Caso base: si n es menor que 10, devolver una lista con n
    if n < 10:
        return [n]
    # Caso recursivo: llamar a la función con n // 10 y agregar el último dígito n % 10
    else:
        return descomponer_numero(n // 10) + [n % 10] #la funcion se llama a si misma y suma su ultimo digito(n % 10), para al final juntarlos y ponernos en una lista como digitos separados 
    