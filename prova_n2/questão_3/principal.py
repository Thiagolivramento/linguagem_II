#from pymongo import MongoClient

from cadastra import Cadastra

#conexao = MongoClient('localhost', 27017)
#banco = conexao.prova
#pessoas = banco.pessoa

def main():
    while(1):
        opcao = input('|----Menu----|'
                      '\n|1-Cadastrar |'
                      '\n|2-Editar    |'
                      '\n|3-Remover   |'
                      '\n|4-Consultar |'
                      '\n\nEscolha uma das opções acima: ')
        if opcao == '1':
            cadastro=Cadastra()
            cadastro.cadastra()
        elif opcao == '2':
            editar()
        elif opcao == '3':
            remover()
        elif opcao == '4':
            consultar()
        else:
            print('\n-OPÇÃO NÃO RECONHECIDA! ESCOLHA UMA DA LISTA DO MENU!-\n')

main()
