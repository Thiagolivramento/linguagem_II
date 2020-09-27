status = True

while True:
    print('Digite uma nota VALIDA, no caso entre: 0 e 10:')
    note = int(input())
    if note >= 0 and note <= 10:
        break
    else:
        print('Nota invalida!! Digite uma nota ENTRE 0 e 10')

print("Parabens! Você digitou uma nota certa!")
