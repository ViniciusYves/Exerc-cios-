'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas são maiores'''

from time import sleep
idade = 0
lista_menores = []
lista_maiores = []
for pessoas in range(0, 7):
    idade += 1
    idade_pessoas = int(input(f"Digite a idade do aluno {idade}: "))
    if idade_pessoas < 18:
        lista_menores.append(idade_pessoas)
    else:
        lista_maiores.append(idade_pessoas)
print("Processando...")
sleep(1)
print(
    f"Os alunos \033[32m{str (lista_maiores)[1:-1]}\033[m são maiores de idade e os alunos \033[31m{str (lista_menores)[1:-1]}\033[m são menores!"
)
print("FIM!")

# Este exercício foi corrigido em vídeo e está correto!