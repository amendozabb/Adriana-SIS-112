import funcioness as fun 
import time
lisP=[]
lisA=[]

while True:
  print(""" MENU 
  1. Crear una lista personalizada de n números
  2. Crear una lista aleatoria de n números sin repetidos
  3. Buscar un número en la lista usando búsqueda lineal
  4. Buscar un número en la lista usando búsqueda binaria
  5. Descomponer un número en sus dígitos usando recursión
  6. Salir""")
  opcion=int(input("Eliga una opcion: "))

  if opcion == 1: # Opción 1: Crear lista manualmente
    listaP = fun.lista_personalizada(n,listaP)
    print(f"Lista manual creada: {listaP}")

  elif opcion == 2: # Opción 2: Generar lista aleatoria de números únicos
    n = int(input("Ingrese el tamaño de la lista aleatoria: "))
    listaA = fun.lista_aleatoria(n,listaA)
    print(f"Lista aleatoria generada: {listaA}")
 
  elif opcion == 3: #Opcion para encontar en numero con busqueda lineal
    num=int(input("Ingrese el numero a encontrar:"))
    lista=("En que lista desea encontrar el numero: Lista personalizada o lista aleatoria (1 para pa primera, 2 para la segunda)")
    if lista == 1:
     inicio=time.time() #tiempo para encontrar el numero
     resultado=fun.busqueda_lineal(num,listaP)
     fin= time.time()
     print(f"Tiempo transcurrido en encontrar el numero \n {(fin-inicio)*1000}ms") #fin del tiempo
    elif lista== 2:
     inicio=time.time() #tiempo para encontrar el numero
     resultado=fun.busqueda_lineal(num,listaA)
     fin= time.time()
     print(f"Tiempo transcurrido en encontrar el numero \n {(fin-inicio)*1000}ms") #fin del tiempo
    else:
      print("Opcion invalida")

  elif opcion== 4:
    num=int(input("Ingrese el numero a encontrar:"))
    lista=("En que lista desea encontrar el numero: Lista personalizada o lista aleatoria (1 para pa primera, 2 para la segunda)")
    if lista == 1:
     inicio=time.time() #tiempo para encontrar el numero
     resultado=fun.busqueda_binaria(num,listaP)
     if resultado != -1:
       print(f"=========\n, El número {num} se encuentra en la posición {resultado}")
     else:
       print(f"=========\n,El número {num} no está en la lista")
     fin= time.time()
     print(f"Tiempo transcurrido en encontrar el numero \n {(fin-inicio)*1000}ms") #fin del tiempo

    elif lista== 2:
     inicio=time.time() #tiempo para encontrar el numero
     resultado=fun.busqueda_binaria(num,listaA)
     if resultado != -1:
       print(f"=========\n, El número {num} se encuentra en la posición {resultado}")
     else:
       print(f"=========\n,El número {num} no está en la lista")
       fin= time.time()
       print(f"Tiempo transcurrido en encontrar el numero \n {(fin-inicio)*1000}ms") #fin del tiempo
    else:
      print("Opcion invalida")

  elif opcion == 5:
   n = int(input("Ingresa un número entero positivo: ")) #se pide el numero a descomponer 
   if n < 0:
        print("Por favor, ingresa un número entero positivo.")
   else:
        # Llamar a la función y mostrar el resultado
        resultado = fun.descomponer_numero(n)
        print("Los dígitos del número son:", resultado)

  elif opcion==6:
    print("Saliendo del sistema...")
    break     



 

   
