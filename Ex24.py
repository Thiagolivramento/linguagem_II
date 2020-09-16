class Classe:
    def uniao(self, lista1, lista2):
        print(f"União = {lista1 + lista2}")
    
    def intercalacao(self, lista1, lista2):
        newLista = []
        for i in range(len(lista1)): 
            newLista.append( lista1[i])
            newLista.append( lista2[i])
        print(f'Intercalação = {newLista}')
        
    
resultado = Classe();

lista1 = [1, 2, 3, 4, 5]
lista2 = ['a', 'b', 'c', 'd', 'e']

resultado.uniao(lista1, lista2)
resultado.intercalacao(lista1, lista2)
