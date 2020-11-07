
class Cadastra:

    def cadastra(self):
        try:
            nome = input('\nNome: ')
            cpf = input('\nCPF: ')
            email = input('\nE-mail: ')

            pessoas.insert_one(
                {
                    "nome": nome,
                    "cpf": cpf,
                    "email": email
                }
            )
            print('\n-Dado inserido com sucesso-\n')

        except Exception as e:
            print("Erro ao cadastrar!")
            print(e)
