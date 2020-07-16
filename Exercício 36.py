from time import sleep
print ("\033[33m-=-\033[m"*40)
print ("Escreva um algoritmo que leia um número inteiro qualquer e peça para o usuário escolher qual será sua base de conversão\n"
       "Binária, Octal ou Hexadecial.")
print ("\033[33m-=-\033[m"*40)
numero = int (input ("Digite um número para iniciar: "))
escolha_conversao = input ("Em qual base será feita a conversão: Binário, Octal ou Hexadecimal? ").strip().capitalize()
print ("Efetuando conversão...")
sleep (3)
if escolha_conversao == "Binário":
    print (f"\033[1;33m{numero}\033[m em representação binária equivale a \033[1;33m{bin(numero)[2:]}\033[m")
elif escolha_conversao == "Octal":
    print (f"\033[1;33m{numero}\033[m em representação Octal equivale a \033[1;33m{oct(numero)[2:]}\033[m")
elif escolha_conversao == "Hexadecimal":
    print (f"\033[1;33m{numero}\033[m em representação Hexadecimal equivale a \033[1;33m{hex(numero)[2:]}\033[m")
else:
    print ("Escolha uma opção valida.")

#Este exercício foi corrigido em aula e está correto!