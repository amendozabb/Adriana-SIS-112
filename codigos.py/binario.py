import listafun as lis
import busquedabinaria as bi 
import time 

listaNum=[]
listComp= int(input("Ingrese la cantidad de datos para la lista:"))
max= int(input("Ingrese el maximo numeros a generar:"))
min=int(input("Ingrese el minimo numero a generar:"))

inicio=time.time()
lis.generarLista(listComp,min,max,listaNum) #se llama a la funcion del otro archivo
print(listaNum)
print(len(listaNum))
print(type(listaNum))
fin= time.time()
print(f"Tiempo transcurrido de la generacion de la lista \n {(fin-inicio)*1000}ms")

#encontrar numero 
num= int(input("Ingresa el numero a encontrar"))
bi.busqueda_binaria(listaNum, num)
