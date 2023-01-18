from math import ceil
print('Loja de Tintas São José')
tamanho = float(input('Informe o tamanho da parede em m²: '))
quant_litros = tamanho / 6
lata = quant_litros / 18
galao = quant_litros / 3.6
dinheiro_lata = lata * 80
dinheiro_galao = galao * 25
print(f'Seria necessário {ceil(lata)} latas de 18L, custando R${dinheiro_lata:.2f} ou {ceil(galao)} galões de 3,6L, custando R${dinheiro_galao:.2f}.')
