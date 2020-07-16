'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50'''
from time import sleep
print("\033[33m{:^55}\033[m".format("Contador de pares e impares"))
escolha = str(
    input(
        "Você gostaria de ver os números pares ou impares do intervalo 1/50? ")
).capitalize().strip()
print("Verificando...")
sleep(1)
if escolha == "Pares":
    print("Os números pares entre 0 e 50 são: ", end="")
    for contagem in range(2, 51, 2):
        print(f"\033[33m{contagem}\033[m, ", end="")
elif escolha == "Impares":
    print("Os números impares entre 0 e 50 são: ", end="")
    for contagem in range(1, 50, 2):
        print(f"\033[33m{contagem}\033[m, ", end="")
else:
    print("Selecione uma opção valida!")

# O exercício foi corrigido em vídeo e está correto!
