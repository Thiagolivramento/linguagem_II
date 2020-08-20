'''Ler um valor e escrever se é positivo ou negativo (considere o valor zero como
positivo)'''

numero = float(input('Digite um número: '))
resto = numero % 2

if numero == 0:
    print('Número par!')
else:
    print('Número é ímpar!')