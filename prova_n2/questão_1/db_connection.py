import psycopg2

class Connection():

    def get_connection(self):
        connection = psycopg2.connect(
            user="postgres",
            password="slayer82",
            host="localhost",
            port="5432",
            database="prova")
        return connection
