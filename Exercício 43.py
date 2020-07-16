'''Elabore um algoritmo que calcule o valor a ser pago por um produto, considerando o seu preço normal e condições de pagamento:\n"
"A vista em dinheiro ou cheque: 10% de desconto;\n"
"A vista no cartão: 5% de desconto;\n"
"Em até 2x no cartão: preço normal;\n"
"3x ou mais no cartão: 20% de juros.'''

print ("\033[33m{:^40}\033[m".format("Lojas Exemplo"))
preco_do_produto = float (input ("Insira o valor do produto desejado: R$ "))

print ('''FORMAS DE PAGAMENTO
[ 1 ] À vista Dinheiro/ Cheque
[ 2 ] À vista Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais no Cartão''')
opção = int (input ("Escolha uma forma de pagamento: "))

if opção == 1:
    print (f"O valor final do produto equivale a R$ {preco_do_produto - (preco_do_produto * 0.10):.2f}")
elif opção == 2:
    print (f"O valor final do produto equivale a R$ {preco_do_produto - (preco_do_produto * 0.05):.2f}")
elif opção == 3:
    print (f"O valor final do produto equivale a R$ {preco_do_produto:.2f}")
elif opção == 4:
    print (f"O valor final do produto equivale a R$ {preco_do_produto + (preco_do_produto * 0.20):.2f}")
else:
    print ("Digite uma opção válida para continuar")

# Este exercício foi corrigido em vídeo e está correto




