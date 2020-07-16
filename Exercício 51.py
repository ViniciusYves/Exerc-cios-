'''Faça um algoritmo que leia um número e diga se ele é ou não um número primo'''

from time import sleep
numero = int(input("Digite um número para verificação: "))
contador = 0
for teste in range(1, numero + 1):
    if numero % teste == 0:
        contador += 1
if contador <= 2:
    print("Verificando...")
    sleep(1)
    print(f"O número {numero} é primo")
else:
    print("Verificando...")
    sleep(1)
    print(f"{numero} não é primo.")
print("FIM!")

# Este exercício foi corrigido em aula e está correto!