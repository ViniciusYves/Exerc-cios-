print ("="*60)
print ("Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.\n"
       "Para salários superiores a R$ 1.200,00 calcule um aumento de 10%.\n"
       "Para os inferiores ou iguais o aumento é de 15%.")
print ("="*60)

salario = float (input ("Digite o seu salário e verifique um possível reajuste: "))
print (f"Tendo em vista que seu salário é {salario} você receberá um aumento de {salario*0.10}." if salario > 1.200
       else f"Tendo em vista que seu salário é {salario} você receberá um aumento de {salario*0.15}")

# Este exercício foi corrigido em sala de aula e está correto