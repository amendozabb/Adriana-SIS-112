
import conversiones

def Menu():

    print("CONVERSOR DE UNIDADES")
    print("Seleccione un opcion: ")
    print("1.Longuitud(MRE0S a metros )")
    print("2.Masa (de gramos a kilogramos) ")
    print("3.Temperatura (de celcius a Fahrenheit)")
    
    print("4.Opcion no valida. Salir")
while True:
    Menu()


    opcion=int(input("Elige  su opcion: "))
    if opcion==4:
        print("Saliendo de el conversor")
        break

    num=float(input("Ingrese el dato que desea convertir: "))

    if opcion==1 :
        print(f'Resultado:{unidades.longitud(num)}')
    elif opcion==2:
        print(f'Resultado:{unidades.masa(num)}')
    else:
        print(f'Resultado: {unidades.temperatura(num)}')


