# Escreva um algortmo que faça o computador "Pensar" em um número entre 0 e 5 e peça para o usuário tentar descobri-lo.
# O programa deverá escrever na tela se o usuário acertou ou errou.

from random import randint
from time import sleep
selecionado = randint (0,5)
print ("Pensei em um número entre 0 e 5. Consegue adivinhar qual foi?")
tentativa = int (input ("Escolha um número:"))
print("Verificando...")
sleep(2)
print (f"Você acertou! O número sorteado foi {selecionado}" if tentativa == selecionado
       else f"Você não acertou. O número sorteado foi {selecionado}.Tente novamente!")

# Este exercício foi corrigido em vídeo e está correto!