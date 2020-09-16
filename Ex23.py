class Classe:
    def maior(self, lista):
        print(f"Maior = {max(lista)}")

    def soma(self, lista):
        totalSoma = 0
        for item in lista:
            totalSoma += item;
        print(f"Total = {totalSoma}")
    
    def ocorrencia(self, lista):
        totalOcorrencia = 0
        for  item in lista:
            if lista[0] == item:
                totalOcorrencia += 1;
        print(f"Ocorrencias = {totalOcorrencia}")
    
    def media(self, lista):
        total = 0
        for item in lista:
            total += item;
        media = total / len(lista)
        print(f"Media = {media}")
        
    
resultado = Classe();

lista = [1, 4, 1, 5, 6, 28, 4, 45, 22, 17, 98, 1]
print(f'List = {lista}')
resultado.maior(lista)
resultado.soma(lista)
resultado.ocorrencia(lista)
resultado.media(lista)

