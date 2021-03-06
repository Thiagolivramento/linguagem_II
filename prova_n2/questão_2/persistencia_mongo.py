from pymongo import MongoClient

#ATIVIDADE DE PERSISTÊNCIA DE DADOS NO MONGODB - LINGUAGEM DE PROGRAMAÇÃO II
conexao = MongoClient('localhost', 27017)
banco = conexao.prova
musica = banco.music

music = [
    {
        "nome": "Solidarity",
        "autor(a)": "Black Uhuru",
        "genero": "Reggae"
    },
    {
        "nome": "Fela Kuti",
        "autor(a)": "Coffin for Head of State",
        "genero": "African Jazz"
    },
    {
        "nome": "I Love King Selassie",
        "autor(a)": "Black Uhuru",
        "genero": "Reggae"
    },
    {
        "nome": "Children of the Grave ",
        "autor(a)": "Black Sabbath",
        "genero": "Heavy Metal"
    }
]

musica.insert_many(music)

print("-----------------------------------------------------------------")
print("\n Cadastros realizados com sucesso no banco! És um monstro!\n")
print("X")
print("A")
print("B")
print("L")
print("A")
print("U")
print("!")
