from pymongo import MongoClient

conexao = MongoClient('localhost', 27017)
banco = conexao.prova
pessoa = banco.pessoa

class Consulta:

    def consultar(self):
        try:
            opcaoConsulta = input('\nOpção 1 -> consulta via CPF'
                                    '\nOpção 2 -> consulta via email'
                                    '\nDigite sua opção: ')
            if opcaoConsulta == '1':
                consultaCpf = input('\nCPF: ')
                resultado = pessoa.find({"cpf":consultaCpf})
                for consulta in resultado:
                    print(consulta)
            elif opcaoConsulta == '2':
                consultaEmail = input('\nE-mail: ')
                resultado = pessoa.find({"email":consultaEmail})
                for consulta in resultado:
                    print(consulta)
            else:
                print('\n-OPÇÃO NÃO ENCONTRADA! ESCOLHA UMA VÁLIDA!-\n')

        except Exception as e:
            print("Erro ao Consultar!")
            print(e)
