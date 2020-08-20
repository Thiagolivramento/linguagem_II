'''Escreva um algoritmo que solicita ao usuário para digitar um número inteiro positivo,
e mostre-o por extenso. Este número deverá variar entre 1 e 5. Se o usuário introduzir
um número que não pertença a este intervalo, mostre a frase “número inválido”.'''

print('Digite um número de 1 a 5: ')
num = int(input())

if num == 1:
    print('Um')
elif num == 2:
    print('Dois')
elif num == 3:
    print('Três')
elif num == 4:
    print('Quatro')
elif num == 5:
    print('Cinco')
else:
    print('Número Inválido!')
