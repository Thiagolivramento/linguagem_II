quantidade = 1
soma = media = maior = menor = 0
while quantidade <= 10:
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    
media = soma / quantidade
print('média = {}, soma = {}, maior = {}, menor = {}'.format(media, soma, maior, menor))

