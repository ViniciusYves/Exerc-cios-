#"Elabore um algoritmo que faça o computador jogar jokênpô com você.")

from random import choice
from time import sleep

jokenpo = ["Pedra", "Papel", "Tesoura"]
jogada_maquina = choice(jokenpo)
jogada_player = str( input("Pedra, Papel ou Tesoura? : ")).capitalize().strip()

print ("JO...")
sleep(1)
print ("...KÊN...")
sleep(1)
print ("......PO!")


if jogada_maquina == "Pedra" and jogada_player == "Tesoura":
    print ("\033[31mVocê perdeu. Pedra quebra tesoura!\033[m")

elif jogada_maquina == "Pedra" and jogada_player == "Papel":
    print ("\033[32mVocê venceu. Papel embrulha pedra!\033[m")

elif jogada_maquina == "Papel" and jogada_player == "Pedra":
    print ("\033[31mVocê perdeu. Papel embrulha pedra!\033[m")

elif jogada_maquina == "Papel" and jogada_player == "Tesoura":
    print ("\033[32mVocê venceu. Tesoura corta papel!\033[m")

elif jogada_maquina == "Tesoura" and jogada_player == "Papel":
    print ("\033[31mVocê perdeu. Tesoura corta papel!\033[m")

elif jogada_maquina == "Tesoura" and jogada_player == "Pedra":
    print ("\033[32mVocê venceu. Pedra quebra tesoura!\033[m")
else:
    print ("Empatamos o jogo!")


