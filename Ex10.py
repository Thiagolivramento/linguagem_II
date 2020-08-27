soma = 0

for i in range(3):
    nota = float(input('Insira a nota do aluno: '))
    soma += nota

media = soma/3
if media >= 6:
    print('Aprovado')
else:
    print('Reprovado')