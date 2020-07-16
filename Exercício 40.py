print ("\033[33m-=-\033[m"*40)
print ("Elabore um algoritmo que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com sua idade:\n"
       "Até 9 anos: mirim;\n"
       "Até 14 anos: infantil;\n"
       "Até 19 anos: junior;\n"
       "Até 20 anos: sênior;\n"
       "Acima: master.")
print ("\033[33m-=-\033[m"*40)
idade = int (input ("Digite sua idade: "))
if idade <= 9:
    print ("Você se enquadra na categoria mirim!")
elif idade > 9 and idade <= 14:
    print ("Você se enquadra na categoria infantil!")
elif idade > 14 and idade <= 19:
    print ("Você se enquadra na categoria junior")
elif idade > 19 and idade == 20:
    print ("Você se enquadra na categoria sênior!")
else:
    print ("Você se enquadra na categoria master!")

#Este exercício foi corrigido em vídeo eestá correto
