import funciones
productos=[]
precios=[]
while True:
  print("""==== SISTEMA DE GESTIÓN DE INVENTARIO ==== ==== SISTEMA DE GESTIÓN DE INVENTARIO ====
 1. Agregar producto
 2. Eliminar producto
 3. Modificar producto
 4. Mostrar todos los productos
 5. Calcular valor total del inventario
 6. Obtener producto más caro y más barato
 7. Salir""")
  
  opcion = int(input("Elige una opcion:"))
  if opcion == 7:
    print("Saliendo del sistema...")
    break
  elif opcion == 1:
    funciones.agregar(productos,precios) 

  elif opcion == 2:
    funciones.mostrar(productos,precios)
    funciones.eliminar(productos, precios)

  elif opcion == 3:
    funciones.mostrar(productos,precios)
    funciones.modificar(productos, precios)
  
  elif opcion== 4:
    funciones.mostrar(productos, precios)
  
  elif opcion== 5:
    funciones.total(precios)
  
  elif opcion == 6:
    funciones.maxmin(precios)
  
  else:
    print("Invalido")
