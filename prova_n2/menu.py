import pypyodbc
import db_connection as dbConn
from read import Read
from create import Create
from update import Update
from delete import Delete

def main():
    print('Opções: C=criar, R=leitura, U=Update, D=Delete ')
    choice = input('Escolha sua opção = ')

    if choice == 'C':
        createObj=Create()
        createObj.func_CreateData()
    elif choice == 'R':
        readObj =  Read()
        readObj.func_ReadData()
    elif choice == 'U':
        updateObj = Update()
        updateObj.func_UpdateData()
    elif choice == 'D':
        deleteObj = Delete()
        deleteObj.func_DeleteData()
    else:
        print('Escolha desconhecida. Selecione uma opção válida!.')

# Call the main function
main()
