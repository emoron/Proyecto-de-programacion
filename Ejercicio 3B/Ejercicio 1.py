#EJERCICIO 1
#Alejandro Nava Castillo
import math as m
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-6,2)
y=(x**2)-(4*x)+5
plt.plot(x,y,linewidth=3,color='r',label='Linea 1')
plt.legend()
plt.title("Grafica A")
plt.xlabel('Tiempo')
plt.ylabel('Aburrimiento')
plt.grid(True)
plt.show()
#b
x=np.linspace(-1,5)
y=2*(x**2)-(8*x)-11
plt.plot(x,y,linewidth=3,color='b',label='Linea 3')
plt.legend()
plt.title("Grafica B")
plt.xlabel('Tiempo')
plt.ylabel('Aburrimiento')
plt.grid(True)
plt.show()
#c
t=np.linspace(-1,5)
y=t*m.e**-2*t
plt.plot(x,y,linewidth=3,color='y',label='Linea 3')
plt.legend()
plt.title("Grafica C")
plt.xlabel('Tiempo')
plt.ylabel('Aburrimiento')
plt.grid(True)
plt.show()
#d
t=np.linspace(0,24)
y=(m.e**-0.1*t)*np.sin(2*t)
plt.plot(x,y,linewidth=3,color='grey',label='Linea 4')
plt.legend()
plt.title("Grafica D")
plt.xlabel('Tiempo')
plt.ylabel('Aburrimiento')
plt.grid(True)
plt.show()
