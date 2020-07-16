'''Refaça o desafio dos triângulos, acrescentando o resco de mostrar que tipo de triângulo será formado:\n"
       "Equilátero: todos os lados iguais;\nIsósceles: dois lados iguais;\nEscaleno: todos os lados diferentes.'''


ladoA = float ( input ("Insira o primeiro valor: "))
ladoB = float ( input ("Insira o segundo  valor: "))
ladoC = float ( input ("Insira o terceiro valor: "))

if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoB + ladoA:
    if ladoA == ladoB == ladoC:
        print ("Os números digitados formam um triângulo equilátero!")
    elif ladoA == ladoB != ladoC or ladoB == ladoC != ladoA or ladoC == ladoB != ladoA:
        print ("Os números digitados formam um triângulo isósceles!")
    else:
        print ("Os números digitados formam um triângulo escaleno!")
else:
    print ("Os números digitados não formam um triângulo")

# Este exercício foi corrigido em vídeo e está correto!