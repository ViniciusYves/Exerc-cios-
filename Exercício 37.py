print ("\033[33m-=-\033[m"*50)
print ("Escreva um programa que leia dois números inteiros, compare-os e mostra na tela qual o maior, menos ou se possuerm valores iguais")
print ("\033[33m-=-\033[m"*50)
numero_um = int (input ("Digite um número: "))
numero_dois = int (input ("Digite um segundo número: "))
lista_de_numeros = [numero_um, numero_dois]
if numero_um > numero_dois or numero_dois > numero_um:
    print (f"O maior número digitado é \033[1;33m{sorted(lista_de_numeros, reverse= True)[0]}\033[m e o menor é \033[1;33m{sorted(lista_de_numeros, reverse= True)[1]}\033[m")
else:
    print ("Os números digitados possuem o mesmo valor!")

#Este exercício foi corrigido em aula e está correto!

