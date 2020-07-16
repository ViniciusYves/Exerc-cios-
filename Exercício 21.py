''' Crie um programa que leia  o nome completo de uma pessoa e mostre:
     - O nome com todas as letras maíusculas;
     - O nome com todas as letras minúsculas;
     - Total de caracteres (sem considerar os espaços);
     - Quantas letras tem o primeiro nome.'''

nome = str (input ("Insira o seu nome completo: ")).strip()
lista = nome.split ()
lista2 = nome.replace (" ","")
print ("{} seu nome pode ser escrito todo em maiúsculo '{}' ou em minúsculo '{}'".format(lista[0],nome.upper(),nome.lower()))
print ("Seu nome completo possuí {} letras e {} estão contidas no primeiro nome".format(len(lista2),len (lista[0])))


# O algoritmo está correto e o exercício foi corrigido em auka
