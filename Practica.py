def imprimir (n):
    if(n%2==0):
        print (n)
    if(n>0):
        return imprimir(n-1) 

imprimir(25)


