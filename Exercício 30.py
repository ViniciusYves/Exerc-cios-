print ("="*90)
print ("Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem cobrando R$0,50")
print ("por KM para viagens de até 200 KM e R$0,45 para viagens mais longas.")
print ("="*90)

distancia = float (input ("Digite a distância que será percorrida durante a viagem: "))
print (f"A viagem custará R${distancia*0.50:.2f} por pessoa!" if distancia <=200.00 else f"A viagem custará R${distancia*0.45:.2f} por pessoa!" )

#Este exercício foi corrigido em aula e está correto!