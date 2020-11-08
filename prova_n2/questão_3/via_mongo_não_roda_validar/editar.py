from pymongo import MongoClient
from validate import Validate

conexao = MongoClient('localhost', 27017)
banco = conexao.prova
pessoa = banco.pessoa

class Editar:

    def edit(self):
        try:
            pesquisar_cpf = input('\nInsira um cpf para editar: ')
            editaNome = input('\nNome: ')
            editEmail = input('\nE-mail: ')


            validarNome = Validate()
            validarNome.validaNome(editaNome)

            validarEmail = Validate()
            validarEmail.validaEmail(editEmail)

            pessoa.update_one(
                {"cpf": pesquisar_cpf},
                {
                    "$set": {
                        "nome": editaNome,
                        "email": editEmail
                    }
                }
            )
            print('\n-ALTERAÇÃO REALIZADA COM SUCESSO!-\n')

        except Exception as e:
            print("Erro ao editar!")
            print(e)
