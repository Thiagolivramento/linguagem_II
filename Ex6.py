numero = int(input('Digite um número para saber se é par ou impar e positivo ou negativo:'))
resto = numero % 2

if resto == 0 and numero >= 0:
    print('Número é par e positivo')
elif resto == 0 and numero < 0:
    print('Número é par e negativo')
elif resto != 0 and numero >= 0:
    print('Número é ímpar e positivo')
elif resto != 0 and numero < 0:
    print('Número é ímpar e negativo')