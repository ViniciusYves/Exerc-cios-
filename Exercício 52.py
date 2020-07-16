'''Elabore um algoritmo que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços'''
palavra = str(input("Digite uma palavra para começar: ")).strip().upper()
frase = palavra.split()
junto = "".join(frase)
inverso = ""
for contrario in range(len(junto) - 1, -1, -1):
    inverso += junto[contrario]
if junto == inverso:
    print(
        f"O conteúdo digitado ({palavra}) é um palindromo, conforme demonstrado a seguir: {inverso}"
    )
else:
    print(f"O conteúdo digitado ({palavra}) não é um palindromo")

# Este exercício foi corrigido em sala e está correto!
# Tive dificuldades com a composição das regras do FOR
