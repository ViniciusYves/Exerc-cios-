#Crie um algoritmo que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la
#Cada litro de tinta pinta uma área de 2m²

print ("Vamos descobrir quantas latas serão necessárias para pintar sua parede?")
largura = float (input ("Digite a largura da sua parede:\n"))
altura = float (input ("Digite a altura da sua parede:\n"))
area = largura*altura
baldes = area/2
print ("Sua parede possuí {}m², portanto serão necessárias {} latas de tinta para pinta-la".format(area,baldes))

#Este exercício fo corrigido em aula