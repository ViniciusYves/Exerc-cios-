'''Elabore um algoritmo que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
 indo de 10 até 0 com umapausa de 1 segundo entre eles.'''
from time import sleep
contagem = int(
    input("Insira uma contagem regressiva para estourar os fogos: "))
for contagem in range(contagem, -1, -1):
    print(contagem)
    sleep(1)
print("\033[1;32mFim da contagem regressiva!\033[m")

# Este exercício foi corrigido em sala de aula e está correto!
