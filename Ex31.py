import math

class Classe:
    def remove(self, dict):
       del dict['Barrabas']
       print(f'Resultado = {dict}')

    
resultado = Classe();

dict = {'Jones': 'Entregador', 'Marijane': 'Advogada', 'Aston': 'Piloto', 'Billy': 'Gerente', 'Barrabas': 'Contador'}
resultado.remove(dict)
