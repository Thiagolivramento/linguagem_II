class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

class Programador(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)

    def aumentaSalario(self):
        self.salario += 20
        print(f'[Dados do Programador] - Nome: {self.nome}, idade: {self.idade} anos. O novo salário é: ${self.salario} reais')

class Analista(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)

    def aumentaSalario(self):
        self.salario += 30
        print(f'[Dados do Analista] - Nome: {self.nome}, idade: {self.idade} anos. O novo salário é: ${self.salario} reais')

class Teste:
    def mostraResultado(self):
        programador = Programador('Peter Tosh', 50, 2000)
        analista = Analista('Gregory Issacs', 56, 3000)

        programador.aumentaSalario()
        analista.aumentaSalario()

resultado = Teste()
resultado.mostraResultado()

