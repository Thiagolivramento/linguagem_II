'''Crie uma classe calculadora com as quatro operações básicas (soma, subtração,
multiplicação e divisão). O usuário deve informar dois números e o programa deve
fazer as quatro operações.'''

class Calculadora:

    def somar(self, x, y):
        soma = x + y
        print(soma)

    def subtrair(self, x, y):
        subtração = x - y
        print(subtração)

    def multiplicar(self, x, y):
        multiplicação = x * y
        print(multiplicação)

    def dividir(self, x, y):
        divisão = x / y
        print(divisão)
//ficou massa ein.
calcular = Calculadora()
x = int(input('Primeiro Número: '))
y = int(input('Segundo Número: '))

calcular.somar(x, y)
calcular.subtrair(x, y)
calcular.multiplicar(x, y)
calcular.dividir(x, y)






