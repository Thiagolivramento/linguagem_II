import psycopg2
from email_validator import validate_email, EmailNotValidError
from db_connection2 import Connection

class Controls():

    def validaName(self, nome):
        valName = True

        if len(nome) == 0 or len(nome) > 150:
            valName = False

        return valName

    def validaCpf(self, cpf):
        valCpf = True

        if len(cpf) == 0 or len(cpf) != 14:
            valCpf = False
        else:
            doubleCpf = self.buscaCPF(cpf)
            if len(doubleCpf) == 1:
                valCpf = False

        return valCpf

    def validateEmail(self, email):
        validEmail = True

        if len(email) > 400:
            validEmail = False

        try:
            valid = validate_email(email)
            valid.email

        except EmailNotValidError as e:
            valEmail = False

        return validEmail

    def salvar(self, nome, cpf, email):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            insert = """INSERT INTO pessoa (nome, cpf, email, deletado) values ('{0}', '{1}', '{2}', 'false');""".format(nome, cpf, email)
            cursor.execute(insert)
            connection.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print("Erro ao salvar", error)

        finally:
            if connection:
                cursor.close()
                connection.close()

    def busca(self, where, param):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            select = f"SELECT nome, cpf, email FROM pessoa WHERE {where}='{param}' AND deletado='false'"
            cursor.execute(select)
            pessoa = cursor.fetchall()

            if len(pessoa):
                for row in pessoa:
                    print(f'Nome = {row[0]}')
                    print(f'CPF = {row[1]}')
                    print(f'E-mail = {row[2]}')
                    print('-------------------')
            else:
                print('Não existe tal registro!')

        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()

    def buscaCPF(self, cpf):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            select = f"SELECT cpf FROM pessoa WHERE cpf='{cpf}'"
            cursor.execute(select)
            data = cursor.fetchall()
            return data

        except (Exception, psycopg2.Error) as error:
            print("Erro!", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()

    def update(self, nome, cpf, email):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            update = f"UPDATE pessoa SET nome='{nome}', email='{email}' WHERE cpf='{cpf}'"
            cursor.execute(update)
            connection.commit()

        except (Exception, psycopg2.Error) as error:
            print("Erro ao atualizar!", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()

    def remove(self, cpf):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            update = f"UPDATE pessoa SET isdelete='true' WHERE cpf='{cpf}'"
            cursor.execute(update)
            connection.commit()

        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()
