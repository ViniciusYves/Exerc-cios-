'''Faça um programa que  calcule a soma entre todos os números ímparesque são multíplos de 3 e que
 se encontram no intervalo de 1 até 500.'''
from time import sleep
nome = 0
print("\033[33m{:^40}\033[m".format("\033[4mSomatória por intervalo\033[m\n"))
intervalo = int(input("Insira um intervalo para realizar a somatória: "))
tipo_de_soma = input(
    "Selecione o tipo de numeração utilizada na soma:\n[ 1 ] PARES\n[ 2 ] IMPARES\nEscolha: "
).capitalize().strip()
s = 0
if tipo_de_soma == "Pares" or tipo_de_soma == "1":
    for contagem in range(0, intervalo + 1, 2):
        s += contagem
    print("Calculando...")
    sleep(1)
    print(
        f"A soma dos números pares do intervalo digitado é:\033[33m{s}\033[m")
elif tipo_de_soma == "Impares" or tipo_de_soma == "2":
    for contagem in range(1, intervalo + 1, 2):
        if contagem % 3 == 0:
            s += contagem
    print("Calculando...")
    sleep(1)
    print(
        f"A soma dos números impares do intervalo digitado é: \033[33m{s}\033[m"
    )
else:
    print("Digite uma opção válida")

# Este exercício foi corrigido em salaeestá correto
