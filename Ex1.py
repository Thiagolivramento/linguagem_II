'''Escreva uma classe que contém um método que calcule se a pessoa é maior de 18 anos ou não. 
Receba os dados pela console e chame este método.'''

class MaiorIdade:
    
    def calcular_idade(self, idade):
        if idade >= 18:
            print('Maior de 18')
        else:
            print('Menor de 18')