print ("="*70)
print ("Faça um programa que leia três números e mostre qual é o maior e qual é o menor!")
print ("="*70)

numero1 = float (input ("Digite o primeiro número: "))
numero2 = float (input ("Digite o segundo  número: "))
numero3 = float (input ("Digite o terceiro número: "))
lista = [numero1,numero2,numero3]
crescente= sorted(lista,reverse=True) #A função sorted é utilizada para organizar números em ordem crescente e o reverse serve pra inverter essa lógica
print (f"O maior número digitado é o {crescente[0]:.1f}, seguido por {crescente[1]:.1f}, portanto o menor é o {crescente[-1]:.1f}!")

# Este exercício foi corrigido em sala de aula e está correto