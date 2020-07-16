#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cidade = str (input ("Insira o nome de sua cidade: ")).strip().capitalize()
lista = cidade.split()
if lista[0] == "Santo":
    print ("A cidade digitada começa com Santo")
else:
    print ("A cidade digitada não começa com Santo")

# Este exercício foi corrigido em aula e está correto
