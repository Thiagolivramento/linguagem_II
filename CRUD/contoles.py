

# Criando a tabela se necessário

class CreateTable:
    def createTable(con):
        with con:

            cur = con.cursor()
            cur.execute("Drop se a tabela Musica existir")
            cur.execute(
                "CREATE TABLE Musica(Id SERIAL PRIMARY KEY, Nome VARCHAR(25), Autor VARCHAR(25), Gênero VARCHAR(25));")
            print ('Tabela música criada!')

# Inserir valores

class InsertData:
    def insertTable(con):
        with con:

            try:
                cur = con.cursor()

                with warnings.catch_warnings():
                    warnings.simplefilter('ignore')
                    cur.execute(
                        "CREATE TABLE IF NOT EXISTS Musica(Id SERIAL PRIMARY KEY, Nome VARCHAR(25), Autor VARCHAR(25), Genero VARCHAR(25));")
                    print ('Tabela música criada!')
                    warnings.filterwarnings('ignore', 'tabela desconhecida!')

                name = raw_input("Nome da música: ")
                autoria = raw_input("Autoria: ")
                gender = raw_input("Gênero: ")
                cur.execute("INSERT INTO Emp  (Nome, Autor, Genero) VALUES(%s, %s, %s)",
                            (name, autoria, gender))
                print ("Dados Inseridos")
                con.commit()
            except Exception as e:
                print (e)

class ReadData:
# Ler registros da tabela
    def retrieveTable(con):
        with con:

            cur = con.cursor(cursor_factory=pdb.extras.DictCursor)
            cur.execute("SELECT * FROM Musica")

            rows = cur.fetchall()
            for row in rows:
                if rows == None:
                    print ('Tabela vazia!')
                    break
                else:
                    print('ID: {0} Nome: {1} Autor: {2} Gênero: {3}'.format(
                        row[0], row[1], row[2], row[3]))

class UpdateData:
# UPDATE registro
    def updateRow(con):
        with con:

            try:
                cur = con.cursor()
                cur = con.cursor(cursor_factory=pdb.extras.DictCursor)
                cur.execute("SELECT * FROM Musica")
                rows = cur.fetchall()
                for row in rows:
                    print('ID: {0} Nome: {1} Autor: {2} Gênero: {3}'.format(
                        row[0], row[1], row[2], row[3]))

                e_id = input("Digite o Id que deseja")
                name = raw_input("Digite o nome que você quer atualizar")
                autoria = raw_input("Digite a autoria que você quer atualizar")
                gender = raw_input("Digite o gênero que você quer atualizar")

                cur.execute("UPDATE Musica SET Nome =%s, Autor = %s, Gênero = %s, WHERE Id = %s",
                            (name, autoria, gender, e_id))

                print ("Número de linhas atualizadas: ",  cur.rowcount)
                if cur.rowcount == 0:
                    print ('Registro não atualizado!')
            except TypeError as e:
                print ('ID não existe!')

class DelData:
#  # Deletar

def deleteRow(con):
    with con:

        try:
            cur = con.cursor()
            cur = con.cursor(cursor_factory=pdb.extras.DictCursor)
            cur.execute("SELECT * FROM Musica")
            rows = cur.fetchall()
            for row in rows:
                print('ID: {0} Nome: {1} Autor: {2} Gênero: {3}'.format(
                    row[0], row[1], row[2], row[3]))

            id = raw_input("Qual é o ID que será deletado?")
            cur.execute("DELETE FROM Musica WHERE Id = %s", id)
            print ("Número de linhas deletadas: ", cur.rowcount)

        except TypeError as e:
            print ('ID não existe!')
