#def busqueda_binaria(lista, numero):
    #print(lista.sort())
   # izquierda, derecha = 0, len(lista) 
  #  while izquierda <= derecha:
        #medio = (izquierda + derecha) // 2
       # if lista[medio] == numero:
      #      return medio
     #   elif numero < lista[medio]:
    #        izquierda = medio +1 
   #     else:
  #          derecha = medio - 1
 #   return -1


def busqueda_binaria(lista, num):
    lista.sort() #reordenar la lista 
    fin =len(lista) - 1
    inicio= 0 
    while inicio <= fin:
        medio =(inicio+ fin) // 2
        print ("=========\n indice del medio:",medio,"\n Valor:",lista[medio])
        if lista[medio]== num:
           return medio
        elif num >lista[medio]:
            inicio=medio +1
        else:
            fin= medio -1
    return -1
    
    


