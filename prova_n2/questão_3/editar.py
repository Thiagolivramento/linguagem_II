
class Editar:

    def edit(self):
        try:
            pesquisar_cpf = input('\nInsira um cpf para editar: ')
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
            print('\n-ALTERAÇÃO REALIZADA COM SUCESSO!-\n')

        except Exception as e:
            print("Erro ao editar!")
            print(e)
