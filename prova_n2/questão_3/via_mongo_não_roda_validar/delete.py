from pymongo import MongoClient

conexao = MongoClient('localhost', 27017)
banco = conexao.prova
pessoa = banco.pessoa

class Delete:

    def remove(self):
        try:
            remove_cpf = input('\nInsira um cpf para remover do sistema: ')
            pessoa.delete_many({"cpf": remove_cpf})
            print('\n-EXCLUSÃO REALIZADA COM SUCESSO!-\n')

        except Exception as e:
            print("Erro ao Deletar!")
            print(e)
