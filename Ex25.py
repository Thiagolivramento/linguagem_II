class Classe:
    def printMetade(self, lista):

        print(f"Resultado = {lista[5:] + lista[:5]}")

        
    
resultado = Classe();

lista = [3, 25, 13, 4, 5, 'h', 'd', 'e', 'g', 'q']

resultado.printMetade(lista)
