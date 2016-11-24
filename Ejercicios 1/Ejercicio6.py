#EJERCICIO 6
#Alejandro Nava Castillo
peso=input("Ingrese Peso(Kg.) ")
h=input("Ingrese Altura(mts.) ")
imc=peso/(h*h)
if imc<16:
    print "Su IMC es " + str(imc) + ", Tiene Delgadez Severa"
elif imc>=16.00 and imc<16.99:
    print "Su IMC es " + str(imc) + ", Tiene Delgadez Moderada"
elif imc>=17.00 and imc<18.49:
    print "Su IMC es " + str(imc) + ", Tiene Delgadez Leve"
elif imc>=18.5 and imc<24.99:
    print "Su IMC es " + str(imc) + ", Tiene Rasgos Normales"
elif imc>=25.00 and imc<29.99:
    print "Su IMC es " + str(imc) + ", Tiene Sobrepeso"
elif imc>=30.00 and imc<39.99:
    print "Su IMC es " + str(imc) + ", Tiene Obesidad"
elif imc>=40.00:
    print "Su IMC es " + str(imc) + ", Tiene Obesidad Morbida"
