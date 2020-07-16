#Crie um programa que leia um número qualquer e mostre na tela se ele é par ou impar.

numero = int (input ("Digite um número e veja se ele é par ou impar: "))
verificar = numero % 2 #todo numero par tem resto de divisão zero
print ("O número digitado é par" if verificar == 0 else "O número digitado é impar")

# O exercício foi corrigido em sala de aula e está correto
