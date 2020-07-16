#Desenvolva um algoritmo que leia o primeiro termo e a razão de uma PA e no final mostre seus dez primeiros termos.

escolha = input(
    "Selecione o tipo de progressão a ser verificado:\n[ 1 ] Aritmética\n[ 2 ] Geométrica\nEscolha: "
)
if escolha == "1" or escolha == "Aritmética":
    razao = int(input("Digite a razão a ser utilizada: "))
    primeiro_termo = int(input("Digite o valor inicial: "))
    p_a = primeiro_termo
    print(f"Os dez primeiros termos da PA correspondem a: ", end="")
    for progressao in range(primeiro_termo, 10):
        p_a = p_a + razao
        print(f"{p_a} ", end=", ")

else:
    razao = int(input("Digite a razão a ser utilizada: "))
    primeiro_termo = int(input("Digite o valor inicial: "))
    p_g = primeiro_termo
    print(f"Os dez primeiros termos da PG correspondem a: ", end="")
    for progressao in range(primeiro_termo, 10):
        p_g = p_g * razao
        print(f"{p_g} ", end="")

print("\nFIM!")

# Este exercício foi corrigido em aula e está correto!
