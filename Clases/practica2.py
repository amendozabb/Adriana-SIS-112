import funciones as fn     
while True:
    fn.interfaz()
    op= int(input())
    if op ==1:
        nota= int(input("Ingrese la nota: "))
        fn.agregar(nota)
    elif op==2:
        nota= int(input("Ingrese el indice de la nota: "))
        fn.eliminar(nota)
    elif op==3:
        indice=int(input("Ingrese el numero de la nota: "))
        nota=int(input("Nota nueva: "))
        fn.modificar(indice, nota)
    elif op==4:
        fn.mostrar()
    elif op==5:
        fn.promedio()
    elif op==6:
        fn.maxmin()