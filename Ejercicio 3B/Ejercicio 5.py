#EJERCICIO 5
#Alejandro Nava Castillo
import matplotlib.pyplot as plt
import numpy as np
import math as m
O=np.linspace(0,2*m.pi)
def valor(ang):
    if ang<0:
        return (ang)*(-1)
    elif ang>0:
        return ang
    else:
        return 0
r=2-2*np.sin(O)+np.sin(O)*(valor(np.cos(O))/(np.sin(O)+1.4))
x=r*(np.cos(O))
y=r*(np.sin(O))
plt.plot(O,d,linewidth=3,color='r')
plt.plot(O,u,linewidth=3,color='g')
plt.show()
