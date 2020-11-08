# CRUD para a disciplina de Linguagem de programação II usando postgres

from controlador2 import Controls

co = Controls()

while True:
    print('--------- MENU ----------')
    print('''[1]:Cadastrar
[2]:Editar
[3]:Remover
[4]:Consultar
[5]:Sair
''')
    print('-------------------')

    option = input(str('Escolha uma opção: '))

    if option == '1':
        print('---CADASTRAR---')
        nome = cpf = email = ''
        while True:
            nome = str(input('Digite o nome: '))
            validName = co.validaName(nome)
            if validName:
                break
            print('NOME INVÁLIDO!')

        while True:
            # Verificar letra dentro do cpf
            print('FORMATO DO CPF: 000.000.000.00')
            cpf = str(input('Digite seu cpf: '))
            validCpf = co.validaCpf(cpf)
            if validCpf:
                break
            print('CPF INVÁLIDO')

        while True:
            email = str(input('Digite o email: '))
            validaEmail = co.validateEmail(email)
            if validaEmail:
                break
            print('EMAIL INVÁLIDO!')

        co.salvar(nome, cpf, email)

    if option == '2':
        print('---EDITAR---')
        while True:
            print('FORMATO DO CPF: 000.000.000.00')
            cpf = str(input('Digite o CPF para fazer alterações: '))
            temCPF = co.buscaCPF(cpf)
            if temCpf:
                nome = str(input('Novo nome: '))
                while True:
                    email = str(input('Novo email: '))
                    validEmail = co.validaEmail(email)
                    if validEmail:
                        break
                    print('EMAIL INVÁLIDO!')
                co.update(nome, cpf, email)
                break
            print('INVÁLIDO!')



    if option == '3':
        print('---REMOVER---')
        while True:
            print('FORMATO DO CPF: 000.000.000.00')
            cpf = str(input('Digite o cpf que deseja remover: '))
            possuiCPF= co.buscaCpf(cpf)
            if len(possuiCPF):
                co.remove(cpf)
                print('Removido com sucesso!')
                break
            print('Inválido, tente novamente!')

    if option == '4':
        print('---CONSULTAR POR---')
        print('''[1]:CPF
[2]:E-MAIL
-------------------
        ''')
        consulta = input(str('Digite a opção para consultar: '))
        if consulta == '1':
            print('FORMATO DO CPF: 000.000.000.00')
            cpf = input(str('Pesquisar pelo cpf: '))
            co.busca('cpf', cpf)
        if consulta == '2':
            email = input(str('Pesquisar pelo e-mail: '))
            co.busca('email', email)

    if option == '5':
        print('---SAIR---')
        break
