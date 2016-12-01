#EJERCICIO 4
#Alejandro Nava Castillo
n=raw_input('Ingrese nombre' )
s=map(str,n)
v=('a','e','i','o','u','A','E','I','O','U')
if n[0]==v[0] or n[0]==v[1] or n[0]==v[2] or n[0]==v[3] or n[0]==v[4]:
    print "La palabra empieza por vocal"
elif n[0]==v[5] or n[0]==v[6] or n[0]==v[7] or n[0]==v[8] or n[0]==v[9]:
    print "La palabra empieza por vocal"
else:
    print "La palabra no empieza por vocal"
