
class Create:
    def func_CreateData(self):

        # chama a conexão com o banco. 
        connection = dbConn.getConnection()
                
        name = input('Nome = ')
        cpf = input('CPF = ')
        email = input('email = ')

        try:
           query = "Insert Into Pessoa(Nome, CPF, email) Values(?,?,?)" 
           cursor = connection.cursor()

           # Executa a query sql
           cursor.execute(query, [name, cpf, email])

           # Commit 
           connection.commit()
           print('Dados salvos com sucesso!')

        except:
             print('Algo deu errado, verifique os dados!')

        finally:
           # Fecha a conexão com o banco
           connection.close()
