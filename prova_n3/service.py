import psycopg2
from init import Connection

class Aluno():

    def create(self, nome, codigo):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            insert = f"insert into public.alunos (nome, codigo) values ('{nome}', '{codigo}');"
            cursor.execute(insert)
            connection.commit()
            return f"Aluno {nome}({codigo}) foi cadastrado no sistema simples"

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
                return 'Nenhum registro foi encontrado no sistema simples'


        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()


    def update(self, codigo):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            update = f"UPDATE from alunos WHERE codigo='{codigo}'"
            cursor.execute(update)
            connection.commit()
            return f'O aluno codigo={codigo} foi atualizado no sistema'

        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()

    def delete(self, codigo):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            update = f"DELETE from alunos WHERE codigo='{codigo}';"
            cursor.execute(update)
            connection.commit()
            return f'O aluno com codigo={codigo} foi deletado do sistema'

        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()


