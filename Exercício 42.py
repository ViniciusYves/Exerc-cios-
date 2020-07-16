'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre um status de acordo com a tabela abaixo:\n"
   Abaixo de 18.5: abaixo do peso;\nEntre 18.5 e 25: peso ideal;\n25 até 30: sobrepeso;\n30 até 40: obesidade;\nAcima de 40: obesidade mórbida'''

peso = float (input ("Digite o seu peso (Kg): "))
altura = float (input ("Digite a sua altura e calcule seu IMC: "))
imc = peso/(altura ** 2)
if imc <= 18.5:
       print ("Você está abaixo do seu peso ideial!")
elif imc > 18.5 and imc < 25:
       print ("Você está com um peso ideal")
elif imc >= 25 and imc < 30:
       print ("Você está um pouco acima do peso!")
elif imc >= 30 and imc < 40:
       print ("Você está obeso, por favor procure um especialista!")
else:
       print ("Consulte um médico!")

# Este exercício foi corrigido em vídeo e está correto!