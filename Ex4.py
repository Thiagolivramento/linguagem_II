'''Faça um programa que receba um valor que é o valor pago, um segundo valor que
é o preço do produto e retorne o troco a ser dado.'''

valor_pago = float(input('Valor pago: '))

preco_produto = float(input('Preço do produto: '))

valor_desconto = float(input('Valor de desconto(%): '))

desconto = valor_desconto/100

novo_valor = preco_produto * (1-desconto)

troco = valor_pago - novo_valor

print('O troco a ser dado é R$', troco)