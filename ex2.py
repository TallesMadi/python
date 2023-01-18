print('Convertor: transformar centímetros e metros')
res = int(input('O valor inicial é em centímetros ou metros? (1 para centímetros e 2 para metros) '))
if res == 1:
    cm1 = float(input('Digite o valor em centímetros: '))
    cm2 = cm1 / 100
    print(f'{cm1} centímetros é igual a {cm2} metros!')
elif res == 2: 
    m1 = float(input('Digite o valor em metros: '))
    m2 = m1 * 100
    print(f'{m1} metros é igual a {m2} centímetros!')
else:
    print(f'O valor {res} inserido está incorreto!')
    