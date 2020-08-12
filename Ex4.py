'''Faça um programa que receba um valor que é o valor pago, um segundo valor que
é o preço do produto e retorne o troco a ser dado.'''

valor_pago = float(input('Valor pago: '))

preco_produto = float(input('Preço do produto: '))

troco = valor_pago - preco_produto

print('O troco a ser dado é R$', troco)