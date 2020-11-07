
class Editar:

    def edit(self):
        try:
            pesquisar_cpf = input('\nPor favor inserir um cpf para editar as informações: ')
            editar_nome = input('\nNome: ')
            editar_email = input('\nE-mail: ')

            pessoas.update_one(
                {"cpf": pesquisar_cpf},
                {
                    "$set": {
                        "nome": editar_nome,
                        "email": editar_email
                    }
                }
            )
            print('\n-Dados alterados com sucesso-\n')

        except Exception as e:
            print("Erro ao editar!")
            print(e)
