#criando uma variavel lista
lista = [] 


#criando uma classe
class Utils:
#função adicionar item na lista
    def add_lista(self, item):
        lista.append(item)
        print(lista)
        print('a) Maior Elemento', max(lista))
        print('b) Soma dos Elementos', sum(lista))


util = Utils()


while True:
    item = int(input("Digite um numero: ou -0 para sair: "))
    util.add_lista(item)
    if item == -0:
        break
