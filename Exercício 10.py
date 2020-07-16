# Crie um algoritmo que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos doláres e euros ela pode comprar.
# Considere que o Dolar equivale a 5 reais e o Euro a 6

v = int (input ("Selecione a moeda a ser convertida:\nDolar (1) ou Euro (2)\n"))
if v == 2:
    print ("Real para Euro:")
    E = float( input("Digite o valor em reais a ser convertido:"))
    print ("O total disponível em Euro é {:.2f}!\n{}!".format(E/6,"Obrigado por usar este conversor"))


elif v == 1:
    print ("Real para Dolar:")
    D = float (input ("Digite o valor em reais a ser convertido:"))
    print ("O total disponível em Dolar é {}!\n{}!".format(D/5,"Obrigado por usar este conversor"))


else:
    print ("Escolha uma das opções acima")


# ESte exercício foi corrigido em aula e está correto!














