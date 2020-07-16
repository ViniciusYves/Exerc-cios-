from time import sleep
print ("\033[36m-=-\033[m"*40)
print ("Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar\no valor da casa, o salárop do comprador e em quantos anos ele vai pagar.")
print ("Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.")
print ("\033[36m-=-\033[m"*40)
print ("\033[33mVERIFICADOR DE EMPRÉSTIMO!\033[m")
casa = float (input ("Insira o valor da casa desejada: "))
print (f"A casa desejada está estimada em R${casa:.3f}.")
parcela = int (input ("Deseja parcelar ela em quantos anos: 10 anos, 20 anos ou 30 anos?\n"))
if parcela == 10:
    mensal =  casa/(12*10)
    print (f"O valor mensal será de R${mensal:.3f} durante dez anos")
    salario = float (input ("Digite seu salário para verificarmos a disponibilidade do empréstimo: "))
    if mensal > (salario*0.30):
        print("Calculando...")
        sleep(2)
        print ("\033[31mDesculpe, você não possuí renda para financiar este imóvel\033[m")
    else:
        print("Calculando...")
        sleep(2)
        print ("\033[32mParabéns, com sua renda o financiamento é viável!\033[m")
elif parcela == 20:
    mensal = casa/(12*20)
    print (f"O valor mensal será de R${mensal:.3f} durante vinte anos")
    salario = float (input ("Digite seu salário para verificarmos a disponibilidae do empréstimo: "))
    if mensal > (salario*0.30):
        print("Calculando...")
        sleep(2)
        print ("\033[31mDesculpe, você não possuí renda para financiar este imóvel\033[m")
    else:
        print("Calculando...")
        sleep(2)
        print ("\033[32mParabéns, com sua renda o financiamento é viável!\033[m")
else:
    mensal = casa/(12*30)
    print (f"O valor mensal será de R${mensal:.3f} durante trinta anos")
    salario = float (input ("Digite seu salário para verificarmos a disponibilidade do empréstimo: "))
    if mensal > (salario*0.30):
        print("Calculando...")
        sleep(2)
        print ("\033[31mDesculpe, você não possuí renda para financiar este imóvel\033[m")
    else:
        print("Calculando...")
        sleep(2)
        print ("\033[32mParabéns, com sua renda o financiamento é viável!\033[m")


    #Este exercício foi corrigido em aula e está correto