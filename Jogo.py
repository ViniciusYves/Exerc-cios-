import random

comida = [
    "Hambúrguer", "Pizza", "Macarronada", "Frango Assado", "Pudim", "Torrada"
]
animais = [
    "Gato", "Cachorro", "Pássaro", "Golfinho", "Macaco", "Lagartixa", "Barata",
    "Mosca", "leão"
]
bandas = ["Metallica", "Arctic Monkeys", "Slayer", "Pantera"]
paises = [
    "Brasil", "Alemanha", "Chile", "Equador", "Venezuela", "Estados Unidos",
    "Canadá", "Japão"
]
animes = [
    "Naruto", "Dragon Ball", "Boku No Hero", "Dungeon", "Gonden Boy",
    "Mirai Nikki", "Nanatsu no Taizai"
]
series = [
    "Peaky Blinders", "Supernatural", "Game Of Thrones", "Friends", "Suicits"
]
livros = [
    "O Pequeno Principe", "A menina Que Roubava Livros", "Fortaleza Digital",
    "O Estrangeiro", "A Noite Devorou O Mundo"
]
filmes = [
    "Harry Potter", "Senhor Dos Anéis", "Capitão Fantástico",
    "Sociedade Dos Poetas Mortos", "Vingadores"
]

print("=" * 62)
print("Comida, Animais, Bandas, Países, Animes, Séries, Livros ou Filmes")
print("=" * 62)
escolha = str(input("Escolha uma das categorias para começar: "))

if escolha == "Comida":
    palavra = random.choice(comida)
    lista = list(palavra)

    if palavra == "Hambúrguer":
        print("Dica: Os personagens do desenho animado Bob Esponja adoram.")
    elif palavra == "Pizza":
        print("Dica: Forma utilizada para representar divisões.")
    elif palavra == "Macarronada":
        print("Dica: Prato típico da culinária Italiana")
    elif palavra == "Frango Assado":
        print("Dica: Alimento utilizado para representar posições sexuais.")
    elif palavra == "Pudim":
        print("Dica: Doce gelatinoso a base de laticionos .")
    elif palavra == "Torrada":
        print("Dica: alimento contindo no café da manhã da população.")

    palavraoculta = palavra.replace(palavra, "_ " * len(palavra))
    print(palavraoculta)
    primeiraletra = input("Escolha uma letra: ")
    if primeiraletra in palavra:
        print("Daqui eu não consigo passar!!!!!!!!")
'''elif escolha == animais:

elif escolha == bandas:

elif escolha == paises:

elif escolha == animes:

elif escolha == series:

elif escolha == livros:

elif escolha == filmes:'''
