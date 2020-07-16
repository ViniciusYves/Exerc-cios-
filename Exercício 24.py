# Crie um algoritmo que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str (input ("Digite seu nome para começar: ")).strip().capitalize()
nomequebrado = nome.split()
if "Silva" in nomequebrado:
    print ("Você está entre 1/4 da população por possuir Silva no nome")
else:
    print ("Você não possuí Silva no nome")

# O exercício foi corrigido em aula e está correto!!!!