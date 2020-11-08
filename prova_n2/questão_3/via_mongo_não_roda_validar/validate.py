#importando regex para poder usar expressão regular na validação de email
import re

from pymongo import MongoClient

conexao = MongoClient('localhost', 27017)
banco = conexao.prova
pessoa = banco.pessoa

class Validate:

# função de validação de cpf
    def validaCpf(self, cpf):
          if len(cpf) != 14:
            return False
          elif cpf == '000.000.000-00' or cpf == '111.111.111-11' or cpf == '222.222.222-22' or cpf == '333.333.333-33' or cpf == '444.444.444-44' or cpf == '555.555.555-55' or cpf == '666.666.666-66' or cpf == '777.777.777-77' or cpf == '888.888.888-88' or cpf == '999.999.999-99':
            return False
          else:
            return True

# função de validação de email com expressão regular (uso do regex)
    def validaEmail(self, email):
        return re.search(r'^[\w]+@[\w]+\.[\w]{2,4}', email) !=None

# função de validação de nome

    def validaNome(self,nome):
        validNome = True
        if len(nome) == 0 or len(nome)>150:
            validNome = False

            return validNome
