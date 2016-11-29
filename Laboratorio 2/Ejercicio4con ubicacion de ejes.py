#EJERCICIO 4
#Alejandro Nava Castillo
import math as m
n=input("Ingrese Numero De Lados Del Poligono ")
while n<3:
    print "El Numero De Lados Del Poligono Debe Ser Mayor o Igual a 3"
    n=input("Ingrese Numero De Lados Del Poligono ")
l=input("Ingrese Medida Del Lado ")
ejex=input ("Origen en Eje X ")
ejey=input ("Origen en Eje Y ")
while l<2:
    print "Por Favor Ingrese Un Valor Superior A 1"
    l=input("Ingrese Medida Del Lado ")
def cos(angulodec):
    return m.cos(m.radians(angulodec))
def sin(angulodec):
    return m.sin(m.radians(angulodec))
lin=range(0,n)
angulo=((n-2)*180/n)
mangulo=angulo/2
anguloe=180-angulo
centro=[ejex,ejey]
mlado=l/2
hip=mlado/cos(mangulo)
x=[]
y=[]
puntos=[]
for i in(lin):
    valorx=round((centro[0]+((cos(i*anguloe)*hip))),2)
    x.append(valorx)
    valory=round((centro[1]+((sin(i*anguloe)*hip))),2)
    y.append(valory)
for i in(lin):
    punto=(x[i],y[i])
    puntos.append(punto)
for i in(lin):
    print "P[" + str(i+1) + "]= ", puntos[i]
