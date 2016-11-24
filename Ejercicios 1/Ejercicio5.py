#EJERCICIO 5
#Alejandro Nava Castillo
segundos=int(input("Ingrese los segundos: "))
dd=(int(segundos/86400))
hh=(int((segundos-(dd*86400))/3600))
mm=(int((segundos-(dd*86400)-(hh*3600))/60))
ss=(int((segundos-(dd*86400)-(hh*3600)-(mm*60))))
print(str(dd)+"d "+str(hh)+"h "+str(mm)+"m "+str(ss)+"s")
