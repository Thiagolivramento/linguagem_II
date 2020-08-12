'''Escreva um algoritmo que solicita ao usuário para digitar um número inteiro positivo,
e mostre-o por extenso. Este número deverá variar entre 1 e 5. Se o usuário introduzir
um número que não pertença a este intervalo, mostre a frase “número inválido”.'''

print('Digite um número de 1 a 5: ')
numero = int(input())

if numero == 1:
    print('Um')
elif numero == 2:
    print('Dois')
elif numero == 3:
    print('Três')
elif numero == 4:
    print('Quatro')
elif numero == 5:
    print('Cinco')
else:
    print('Número Inválido!')