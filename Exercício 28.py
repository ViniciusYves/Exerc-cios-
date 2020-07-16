# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h mostre uma mensagem dizendo que ele foi multado.
# A multa vai vai custar R$ 7,00 por cada KM acima do limite
print ("="*40)
print ("Velocidade máxima permitida de 80 KM/H")
print ("="*40)
velocidade = int (input ("Qual foi a velocidade máxima registrada? "))
multa = (velocidade-80)*7
if velocidade > 80:
    print ("Você ultrapassou a velocidade máxima permitida prevista, portanto será multado!")
    print (f"A multa possui o valor de 7 reais por KM/H totalizando R${multa:.2f} em multa.")

print ("O veículo não excedeu o limite de velocidade permitido, portanto não será multado")

# Este exercício foi corrigido em vídeo e está correto!