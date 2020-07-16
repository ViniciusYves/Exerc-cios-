# Faça um programa que leie o comprimento do catero oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o valor de sua hipotenusa

from math import sqrt
print ("-"*40)
print ("Calcule os valores de seu triângulo!")
print ("-"*40)
adjacente = float (input ("Digites o valor do seu cateto adjacente: "))
oposto = float (input ("Digite o valor do seu cateto oposto: "))
hipotenusa = float ((adjacente**2)+(oposto**2))
print ("h²= {}² + {}²".format(adjacente,oposto))
print ("h²= {} + {}".format(adjacente**2,oposto**2))
print ("h= √{}".format ((adjacente**2)+(oposto**2)))
print ("h= {:.1f}".format(sqrt(hipotenusa)))

