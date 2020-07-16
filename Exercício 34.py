print ("="*90)
print (" Desenvolva um algoritmo que leia o valor de três retas e diga ao usuário se elas podem ou não formar um triângulo")
print ("="*90)
ladoA = float ( input ("Insira o primeiro valor: "))
ladoB = float ( input ("Insira o segundo  valor: "))
ladoC = float ( input ("Insira o terceiro valor: "))
if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoB +ladoA:
    print ("Os números digitados formam um triângulo")
else:
    print ("Os números digitados não formam um triângulo")

# Este exercício foi corrigido em sala e está correto!