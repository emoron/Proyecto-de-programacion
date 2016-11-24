#EJERCICIO 2
#Alejandro Nava Castillo
interes=0.04
n=input("Cantidad Inicial: ")
saldoN=0
for i in range(4):
    a=interes*n
    saldoN=n+a
    saldof=saldoN+(i*a)
    print saldof
