import psycopg2
from init import Connection

class Aluno():

    def create(self, name, identificador, email):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            insert = f"insert into public.alunos (name, identificador, email) values ('{name}', '{identificador}', '{email}');"
            cursor.execute(insert)
            connection.commit()
            return f" O Aluno {name}({identificador}) foi cadastrado no sistema simples"

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)

        finally:
            if connection:
                cursor.close()
                connection.close()

    def getAll(self):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            select = f"SELECT * FROM alunos;"
            cursor.execute(select)
            aluno = cursor.fetchall()

            if len(aluno):
                return aluno
            else:
                return 'Nenhum registro de aluno foi encontrado no sistema simples'


        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()


    def update(self, identificador):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            update = f"UPDATE alunos SET identificador='{identificador}';"
            cursor.execute(update)
            connection.commit()
            return f'Os dados do aluno com o identificador={identificador} foram atualizados no sistema'

        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()

    def delete(self, identificador):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            update = f"DELETE from alunos WHERE identificador='{identificador}';"
            cursor.execute(update)
            connection.commit()
            return f'Os dados do aluno com o identificador={identificador} foram deletados do sistema'

        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()


