'''Faça um programa que leia o peso de cinco pessoas e no final mostre qual foi o maior e o menor peso lidos'''
from time import sleep
lista_peso = []
pessoa = 0
for peso in range(0, 5):
    pessoa += 1
    KG = int(input(f"Digite o peso da pessoa número {pessoa}: "))
    lista_peso.append(KG)
print("Aguarde...")
sleep(1)
print(
    f'''\033[33mDe todas as cinco pessoas a mais pesada possuí {sorted(lista_peso, reverse= True)[0]} Kg.\nPor outro lado a menos pesada possuí um peso equivalente a {sorted(lista_peso)[0]} Kg!\033[m'''
)

# Este exercício foi corrigido em vídeo e está correto!