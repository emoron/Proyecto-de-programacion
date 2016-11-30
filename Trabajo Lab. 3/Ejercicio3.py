#EJERCICIO 3
#Alejandro Nava Castillo
l=input ("Primer Entero ")
while (l-(int(l)))>0:
        print "No es un Entero, vuelva a ingresar por favor"
        l=input ("Primer Entero ")
m=input ("Segundo Entero ")
while (m-int(m))>0:
        print "No es un Entero, vuelva a ingresar por favor"
        m=input ("Segundo Entero ")
n=input ("Tercer Entero ")
while (n-int(n))>0:
        print "No es un Entero, vuelva a ingresar por favor"
        n=input ("Tercer Entero ")
lista=[l,m,n]
c=max(lista)
d=min(lista)
ubimax=lista.index(c)
ubimin=lista.index(d)
del lista[ubimax]
del lista[ubimin]
print "Menor Valor",d
print "Valor Medio",lista[0]
print "Valor Mayor",c
