'''Elabore um algoritmo que leia o nome, idade e sexo de 4 pessoas. No final mostre: A média de idade do grupo, O nome do homem mais velho e quantas mulheres tem menos de 20 anos.'''
from time import sleep
somaidade = 0
maisvelho = ''
maioridadehomem = 0
media = 0
mulheres = 0
for laço in range(1, 5):
    print(f"------- {laço}ª PESSOA --------")
    sexo = str(input("SEXO [M/F]: "))
    nome = str(input("NOME: "))
    idade = int(input("IDADE: "))
    somaidade += idade
    if laço == 1 and sexo in "Mm":
        maioridadehomem = idade
        maisvelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        maisvelho = nome
    if sexo in "Ff" and idade < 18:
        mulheres += 1

media = somaidade / 4
print("Aguarde...")
sleep(1)
print(f"A média de idade do grupo listado é {media:.0f}.")
print(
    f"O homem mais velho do grupo é o {maisvelho} possuindo {maioridadehomem} anos de idade."
)
print(f"Ao todo são {mulheres} mulheres com menos de 18 anos")
