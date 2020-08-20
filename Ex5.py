'''Ler um valor e escrever se é positivo ou negativo (considere o valor zero como
positivo)'''

#numero = int(input('Digite um número: '))

#if numero >= 0:
#   print('Número positivo!')
#else:
#    print('Número negativo!')

numero = float(input('Digite um número para saber se é par ou impar:'))
resto = numero % 2

if resto == 0:
    print('Número é par')
else:
    print('Número é impar')
