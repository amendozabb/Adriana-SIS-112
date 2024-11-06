def agregar (productos, precios):
    print("====AGREGAR PRODUCTO====")
    product= str(input("Ingrese el nombre del producto:"))
    precio= float(input("Ingresa el precio del producto:"))
    productos.append(product)
    precios.append(precio)
    print("Producto agregado exitosamente")

def eliminar(productos,precios):
    print("====ELIMINAR PRODUCTO===")
    if len(productos) and len(precios) == 0:
        print("No se agregaron productos")
        productos=[]
        precios=[]
        return productos,precios 
    else:
        while True:
          indice=int(input("Ingresa el indice del producto a eliminar (0 para el primer producto, 1 para el segundo, etc.): "))
          if indice >=0  and  indice <=len(productos):
              break
          else:
              print("No existe")
        print("El producto actual es: {}, precio: {}".format(productos[indice-1], precios[indice-1]))
        productos.pop(indice-1)
        precios.pop(indice-1)
        print("El producto se elimino")
        return productos,precios 

def modificar(productos,precios):
    print("====MODIFICAR PRODUCTO====")
    if len(productos) and len(precios) == 0:
        print("No se agregaron productos")
        return productos,precios 
    else:
        while True:
          indice=int(input("Ingresa el indice del producto a modificar (0 para el primer producto, 1 para el segundo, etc.):"))
          if indice >=1  and  indice <=len(productos):
              break
          else:
              print("No existe")
        print("El producto actual es: {}, precio: {}".format(productos[indice-1],precios[indice-1]))
        nuevo_precio= int(input("Ingrese el nuevo precio del producto:"))
        precios[indice-1] = nuevo_precio
        print("El producto se modifico exitosamente")
        return precios 
    
def mostrar(productos,precios):
       print("====MOSTRAR PRODUCTOS====")
       if len(productos)== 0:
         print("No se agregaron productos")
       else:
           for i in range(len(productos)):
            print("Producto {}: {} , precio por unidad: {}".format((i+1), productos[i], precios[i]))
           
def total(precios):
    total= sum(precios)
    print(f"El valor total del inentario es: {total}")

def maxmin(precios):
    print("====PRODUCTO MAS CARO Y MAS BARATO====")
    if len(precios) == 0:
        print("No hay notas para sacar minimo o maximo")
    else:
        print("El producto mas caro: {}". format(max(precios)))
        print("El producto mas barato: {}". format(min(precios)))