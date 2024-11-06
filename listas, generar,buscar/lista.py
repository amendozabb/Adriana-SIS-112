import listafun as lis
import time
listaNum=[]
listComp= int(input("Ingrese la cantidad de datos para la lista:"))
max= int(input("Ingrese el maximo numeros a generar:"))
min=int(input("Ingrese el minimo numero a generar:"))

#tiempo en generar lista
inicio=time.time()
lis.generarLista(listComp,min,max,listaNum) #se llama a la funcion del otro archivo
print(listaNum)
print(len(listaNum))
print(type(listaNum))
fin= time.time()
print(f"Tiempo transcurrido de la generacion de la lista \n {(fin-inicio)*1000}ms")


#funcion para encontar un numero
inicio=time.time() #tiempo para encontrar el numero
num=int(input("Ingrese el numero a encontrar:"))
lis.encontrarLista(num, listaNum)
fin= time.time()
print(f"Tiempo transcurrido en encontrar el numero \n {(fin-inicio)*1000}ms") #fin del tiempo 







