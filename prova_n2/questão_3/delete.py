
class Delete:

    def remove(self):
        try:
            remove_cpf = input('\nInsira um cpf para remover do sistema: ')
            pessoas.delete_many({"cpf": remove_cpf})
            print('\n-EXCLUSÃO REALIZADA COM SUCESSO!-\n')

        except Exception as e:
            print("Erro ao Deletar!")
            print(e)
