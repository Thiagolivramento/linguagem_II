import psycopg2

# classe que executa a conexão com o banco
class Connection():

    def getConnection(self):
        connection = psycopg2.connect(
            user="postgres",
            password="slayer82",
            host="localhost",
            port="5432",
            database="prova")
        return connection
