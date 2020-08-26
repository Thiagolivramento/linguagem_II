numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

if numero1 == numero2:
    print('Proibido digitar número iguais!')
elif numero1 > numero2:
    print('O primeiro número é maior que o segundo!')
else:
    print('O segundo número é maior que o primeiro!')