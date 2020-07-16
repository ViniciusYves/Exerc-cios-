# Desenvolva um programa que leia as quatro notas de um aluno, calcule sua média e mostre o resultado final

print ("Bom dia, professor! Peço por gentileza que insira as notas do seu aluno:")
n1 = float (input ("Atividade 1:"))
n2 = float (input ("Trabalho:"))
n3 = float (input ("Atividade 2:"))
n4 = float (input ("Atividade final:"))
n5 = (n1 + n2 + n3 + n4)/4
if n5 >= 5:
    print("A média do aluno é {:.1f} e ele foi aprovado!".format(n5))

else:
    print ("A média do aluno é {:.1f} e ele foi reprovado!".format (n5))


# Este exercício foi corrigido e está correto