
""" Decorator permite adicionar comportamento em um objeto em tempo de execução (forma dinâmica).
Ou seja, ele agrega responsabilidades a um objeto e permitindo a expansão do objeto de maneira mais flexivel.
Dessa forma, podemos expandir uma instância sem precisar utilizar herança, somente composição.
No código mais abaixo, temos um exemplo."""

""" Padrão de projeto:  são soluções para os problemas comuns que encontramos no desenvolvimento de um software ou durante a manutenção de
um software orientado ao objeto. Como apontou Rossi: 'Os padrões de projeto são soluções para problemas que alguém já teve e resolveu. 
Eles foram resolvidos aplicando um modelo que foi documentado e que você pode adaptar inteiramente ou de acordo com a necessidade de uma solução.' """
""" Fonte:https://medium.com/@giselezrossi/decorator-with-python-dba2016706cf """




import time
import random

def f1(func):
    def wrapper():
        before = time.time()
        func()
        print(f'A função foi executada em {time.time() - before} segundos')

    return wrapper

@f1
def f():
    soma = 0
    for i in range(4):
        soma += random.randint(0, 100)
    print(f' O valor total da soma foi = {soma}')
f()
