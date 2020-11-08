from pymongo import MongoClient
from validate import Validate

conexao = MongoClient('localhost', 27017)
banco = conexao.prova
pessoa = banco.pessoa

class Cadastra:

    def cadastra(self):
        try:

            nome = input('\nNome: ')
            validarNome = Validate()
            validarNome.validaNome(nome)

            cpf = input('\nCPF: ')
            validaCpf = Validate()
            validaCpf.validaCpf(cpf)

            email = input('\nE-mail: ')
            validarEmail = Validate()
            validarEmail.validaEmail(email)

            pessoa.insert_one(
                {
                    "nome": nome,
                    "cpf": cpf,
                    "email": email
                }
            )
            print('\n-CADASTRO RELIZADO COM SUCESSO!-\n')

        except Exception as e:
            print("Erro ao cadastrar!")
            print(e)
