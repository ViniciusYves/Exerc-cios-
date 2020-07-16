'''Desenvolva um algoritmo que leia seis números inteiros e mostre apenas a soma daqueles que forem pares. Se o valor for ímpar desconsidere'''
soma = 0
for numeros in range(0, 6):
    Numero = int(input("Digite um número: "))
    if Numero % 2 == 0:
        soma = soma + Numero
print(soma)

# Este exercício foi corrigido em vídeo e está correto!