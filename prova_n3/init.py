import psycopg2

class Connection():

  def getConnection(self):
    connection = psycopg2.connect(user="postgres", password="slayer82", host="localhost", port="5432", database="alunos")

    return connection
