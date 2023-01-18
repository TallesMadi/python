print('Progressão')
divisor = 1
total = 0
quant = int(input('Escolha a quantidade de termos: '))
for c in range(1, quant + 1):
    total += c/divisor
    if c < quant:
        print(f'{c}/{divisor} + ', end='')
    else:
        print(f'{c}/{divisor} = ', end='')
    divisor += 2
print(f'{total:.2f}')
