'''Crie um programa que leia um número real qualquer e mostra na tela a sua porção inteira.
Por exemplo: "Digite um número: '6.127'. O número digitado possuí como parte inteira o número '6'"'''

from math import trunc
valor = float (input ("Digite um número: "))
print ("O valor inteiro do número {} é {}".format (valor, trunc(valor)))

# Este exercício foi corrigido em vídeo e está correto
