#Elabore um algoritmo que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "a";
#Em que posição ela aparece pela primeira vez e em qual aparece pela última.

frase = str (input ("Digite uma frase para análise: ")).strip().lower()
quebradefrase = list(frase)
conteA = quebradefrase.count("a")
primeiroA = frase.find("a")
ultimoA = frase.rfind ("a")
print ("Sua frase possuí o total de {} letras 'a'.\nA primeira vez que ela aparece é na posição {} e a última encontra-se na posição {}".format(conteA,primeiroA+1,ultimoA))

# Este exercício foi corrigido em vídeo e está correto!