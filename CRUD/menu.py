



def main():
    print('Opções: C=Criar, R=Ler, U=Atualizar, D=Deletar ')
    choice = input('Escolha uma opção = ')

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
        print('Escolha inválida.')

# chamando a função main
main()
