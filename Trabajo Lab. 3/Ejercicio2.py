#EJERCICIO 2
#Alejandro Nava Castillo
n=input("Ingrese Numero A Evaluar ")
while n>9999:
    print"Ingrese un Numero Menor a 4 digitos"
    n=(input("Ingrese Numero A Evaluar "))
while n<1000:
    print"Ingrese un numero con al menos 4 digitos"
    n=(input("Ingrese Numero A Evaluar "))
nc=str(n)
suman=int(nc[0])+int(nc[1])+int(nc[2])+int(nc[3])
print "La suma de los digitos individuales es ",suman
