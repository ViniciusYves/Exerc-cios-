# O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos trabalhos dos alunos.
# Faça um programa que leia o nome dos alunos e mostre a ordem sorteada.

import random
print ("-"*47)
print ("Defina a ordem de apresentação dos trabalhados: ")
print ("-"*47)
aluno1 = input ("Insira o nome do aluno (1): ")
aluno2 = input ("Insira o nome do aluno (2): ")
aluno3 = input ("Insira o nome do aluno (3): ")
aluno4 = input ("Insira o nome do aluno (4): ")
alunos = (aluno1, aluno2, aluno3, aluno4)
sorteio = random.sample (alunos,4)
print ("A ordem de apresentação é: {}".format(sorteio))

#Este exercício foi corrigido e está correto