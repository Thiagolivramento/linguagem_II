from controlador import Controlador

control = Controlador()

count = 0

while count < 6:
    id = str(input("Digite o id da música: "))
    nome = str(input("Digite o nome da música: "))
    autoria = str(input("Digite o nome do(a) autor(a): "))
    genero = str(input("Digite o gênero musical: "))
    count = count+1
    control.save(id,nome, autoria, genero)
    pass
