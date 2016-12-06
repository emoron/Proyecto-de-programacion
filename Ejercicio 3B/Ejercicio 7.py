#EJERCICIO 6
#Alejandro Nava Castillo
import matplotlib.pyplot as plt
import numpy as np
import math as m
u=np.linspace(0,2*m.pi,0.015)
r=150+100*np.sin(4.5*u)
l=u-(np.cos(10*u)/10)
x=320+r*np.cos(l)
y=-240-r*np.sin(l)
plt.plot(u,x,linewidth=3,color='r')
plt.plot(u,y,linewidth=3,color='g')
plt.show()
