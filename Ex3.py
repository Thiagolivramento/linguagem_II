'''Crie uma classe calculadora com as quatro operações básicas (soma, subtração,
multiplicação e divisão). O usuário deve informar dois números e o programa deve
fazer as quatro operações.'''

class Calculadoramaisum:

    def somar(self, x, y):
        soma = (x + y) + 1
        print(soma)

    def subtrair(self, x, y):
        subtração = (x - y) + 1
        print(subtração)

    def multiplicar(self, x, y):
        multiplicação = (x * y) + 1
        print(multiplicação)

    def dividir(self, x, y):
        divisão = (x / y) + 1
        print(divisão)

calcular = Calculadora()
x = int(input('Primeiro Número: '))
y = int(input('Segundo Número: '))

calcular.somar(x, y)
calcular.subtrair(x, y)
calcular.multiplicar(x, y)
calcular.dividir(x, y)






