lista = []
maior = menor = 0
for n in range(5):
    lista.append(int(input(f"Digite a quantidade de presos no {n + 1}º mês: ")))
    if n == 0:
        maior = menor = lista[n]
    else:
        if lista[n] > maior:
            maior = lista[n]
        if lista[n] < menor:
            menor = lista[n]

print(f'O mês com o maior número de capturados foi {maior}')
print(f'O mês com o menor número de capturados foi {menor}')

total = 0
for item in lista:
    total += item;
media = total / len(lista)
print(f"A media de capturados nos meses é de {media}")

diffList = []
for n in range(5):
    diffList.append(abs(media - lista[n]))

menorAprox = indexMenor = None
for key, value in enumerate(diffList):
    if key == 0:
        menorAprox = value
    else:
        if value < menorAprox:
            menorAprox = value
            indexMenor = key

print(f'O valor aproximado da média de capturados foi de {lista[indexMenor]}')
