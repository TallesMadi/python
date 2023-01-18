print('Progressão')
h = 0
quant = int(input('Escolha uma quantidade de termos: '))
for c in range(1, quant + 1):
    h += 1/c
    if c < quant:
        print(f'1/{c} + ', end='')
    else:
        print(f'1/{c} = ', end='')
print(h)
