import listafun as lis
import busquedabinaria as bi 
import time 

lista=[]
listComp= int(input("Ingrese la cantidad de datos para la lista:"))
max= int(input("Ingrese el maximo numeros a generar:"))
min=int(input("Ingrese el minimo numero a generar:"))

inicio=time.time()
lis.generarLista(listComp,min,max,lista) #se llama a la funcion del otro archivo
print(lista)
print(len(lista))
print(type(lista))
fin= time.time()
print(f"Tiempo transcurrido de la generacion de la lista \n {(fin-inicio)*1000}ms")

#encontrar numero 
num= int(input("Ingresa el numero a encontrar:"))
resultado = bi.busqueda_binaria(lista, num)
if resultado != -1:
    print(f"=========\n, El número {num} se encuentra en la posición {resultado}")
else:
    print(f"=========\n,El número {num} no está en la lista")
