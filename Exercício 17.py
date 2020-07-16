# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo e escrevendo os nomes escolhidos

from random import choice
print ("Insira abaixo os nomes dos alunos a serem sorteados:")
aluno1 = input ("Insira o nome do primeiro aluno (1): ")
aluno2 = input ("Insira o nome do segundo aluno (2): ")
aluno3 = input ("Insira o nome do terceiro aluno (3): ")
aluno4 = input ("Insira o nome do quarto aluno (4): ")
alunos = [aluno1, aluno2, aluno3, aluno4]
sorteado= choice (alunos)
print ("O aluno que apagará o quadro é o {}".format(sorteado))

#Este exercício foi corrigido em vídeo e está correto