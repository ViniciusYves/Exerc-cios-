print ("\033[33m-=-\033[m"*47)
print ("Elabore um algoritmo que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a nota atingida.")
print ("\033[33m-=-\033[m"*47)
nota_um = float (input ("Digite o valor da primeira nota: "))
nota_dois = float (input ("Digite o valor da segunda nota: "))
media = (nota_um+nota_dois)/2
if media < 5:
    print (f"\033[31mAluno possuí média {media}, portanto foi reprovado!\033[m")
elif 6.9 > media >= 5 and media :
    print (f"\33[33mAluno possuí média {media}, portanto está de recuperação!\033[m")
else:
    print (f"\033[32mAluno possuí média {media}, portanto está aprovado!\033[m")

#Este exercício foi corrigido em vídeo e está correto!