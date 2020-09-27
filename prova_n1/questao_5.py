import time

class MostraMensagem:
    def codigo(self, lista):
        print(f'Código = {lista}')
        msg = []
        for item in lista:
            if item == 1:
                msg.append('a')
            elif item == 2:
                msg.append('b')
            elif item == 3:
                msg.append('c')
            elif item == 4:
                msg.append('d')
            elif item == 5:
                msg.append('e')
            elif item == 6:
                msg.append('f')
            elif item == 7:
                msg.append('g')
            elif item == 8:
                msg.append('h')
            elif item == 9:
                msg.append('i')
            elif item == 10:
                msg.append('j')
            elif item == 11:
                msg.append('k')
            elif item == 12:
                msg.append('l')
            elif item == 13:
                msg.append('m')
            elif item == 14:
                msg.append('n')
            elif item == 15:
                msg.append('o')
            elif item == 16:
                msg.append('p')
            elif item == 17:
                msg.append('q')
            elif item == 18:
                msg.append('r')
            elif item == 19:
                msg.append('s')
            elif item == 20:
                msg.append('t')
            elif item == 21:
                msg.append('u')
            elif item == 22:
                msg.append('v')
            elif item == 23:
                msg.append('w')
            elif item == 24:
                msg.append('x')
            elif item == 25:
                msg.append('y')
            elif item == 26:
                msg.append('z')
            elif item == 0:
                msg.append(' ')
        msgCompacta = ''
        for item in msg:
            msgCompacta += item
        print(f'Decifrando a mensagem!')
        time.sleep(2)
        print(f'A mensagem é: {msgCompacta}')


resultado = MostraMensagem()

lista = [13, 1, 18, 9, 10, 21, 1, 14, 1, 0, 14, 15, 23]
resultado.codigo(lista)
