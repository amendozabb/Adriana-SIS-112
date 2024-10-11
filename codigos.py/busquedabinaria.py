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


def busqueda_binaria(lista, objetivo)
    fin =len(lista) - 1
    lista.sort()
    inicio= 0 
    while inicio <= fin:
        medio =(inicio+ fin) // 2
    print ("=========\n",medio)
    if lista[medio]== objetivo:
        return medio
    elif objetivo >lista[medio]:
     inicio=medio +1
    else:
       fin= medio -1
    print(medio)    
    
    


