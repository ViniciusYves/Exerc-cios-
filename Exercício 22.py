#Faça um programa que leia um número de 0 a 999 e monstre na tela cada um de suas casas decimais separadas.

numeral = str( input ("Insira um número entre 0 e 999 para começar: "))
if len(numeral) == 3:
    lista = list(numeral)
    centena = lista[0]+"00"
    dezena = lista[1]+"0"
    unidade = lista[2]
    print ("Se somarmos {} + {} + {} obteremos o numeral digitado ({})".format (centena, dezena, unidade, numeral))
elif len(numeral) == 2:
    lista = list(numeral)
    dezena = lista[0]+"0"
    unidade = lista[1]
    print ("Se somarmos {} + {} obteremos o numeral digitado ({})".format (dezena,unidade,numeral))
elif len(numeral) == 1:
    print (" O número digitado foi {}".format(numeral))
else:
    print ("Por favor digitar um numero válido")

# O exercício foi corrigido em aula, entretanto poderia ter sido executado de uma outra forma.
