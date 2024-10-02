def suma(a,b):
    c = a + b
    print (c) #
    return c 

def resta(x,y):
    c= x-y
    print(c)
    return c

def sumalist(a):
    resultado= sum(a)
    print(resultado)

def p_lista(lista):
    for i in range(len(lista)):
        print(f"indice={i} valor= {lista[i]}")   #combina letrar y enteros 