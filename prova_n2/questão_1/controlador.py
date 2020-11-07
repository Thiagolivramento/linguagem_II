import psycopg2
from db_connection import Connection


class Controlador():

    def save(self, id, nome, autoria, genero):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO musica (id ,nome, autoria, genero) values ('{0}', '{1}', '{2}', '{3}');""".format(id,nome, autoria, genero))
            connection.commit()
            print("Dados inseridos com sucesso!")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
