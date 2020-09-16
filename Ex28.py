import math

class Classe:
    def media(self, lista):
        total = 0
        for item in lista:
            total += item;
        media = total / len(lista)

        print('media',media)
        for item in lista:
            if math.isclose(item, media, abs_tol = 0.50):
                print(f'Valor mais próximo da media é({media}) = {item}')

    
resultado = Classe();

lista = [2.5, 8.3, 4.9, 6.8, 10]
resultado.media(lista)
