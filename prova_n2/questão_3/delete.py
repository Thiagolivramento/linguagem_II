
class Delete:

    def remove(self):
        try:
            remove_cpf = input('\nPor favor inserir um cpf para remover do sistema: ')
            pessoas.delete_many({"cpf":remove_cpf})
            print('\n-Pessoa excluída com sucesso-\n')

        except Exception as e:
            print("Erro ao Deletar!")
            print(e)
