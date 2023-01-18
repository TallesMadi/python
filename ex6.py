print('Sequencia de números diviseis por 7 e não divisiveis por 5 de 1 a 100')
for c in range(0,100):
    if (c % 7 == 0 and c % 5 != 0):
        print(c)