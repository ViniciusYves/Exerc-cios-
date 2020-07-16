print ("="*60)
print ("Desenvolva um programa que leia um ano qualquer e diga se ele é bissexto")
print ("="*60)

ano = int (input ("Insira o ano para verificar se este é bissexto: "))
print (f'{ano} é um ano bi sexto' if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else f"{ano} não é um ano bissexto")

# Este exercício foi corrigido em aula e está correto!