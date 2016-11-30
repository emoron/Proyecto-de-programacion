import math as m
t1=input ("Ingrese Latitud de P1 ")
g1=input ("Ingrese Longitud de P1 ")
t2=input ("Ingrese Latitud de P2 ")
g2=input ("Ingrese Longitud de P2 ")
def rad(x):
    return (x*m.pi)/180
Distancia=6371.01*m.acos(m.sin(rad(t1))*m.sin(rad(t2))+m.cos(rad(t1))*m.cos(rad(t2))*m.cos(rad(g1)-rad(g2)))
print Distancia, "Kilometros"
