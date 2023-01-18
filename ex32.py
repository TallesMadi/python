base = int(input('Escolha a base do número: '))
lista = [base]
expoente = int(input('Escolha o expoente: '))
tot = 0
for c in range(1, expoente):
    tot = base * lista[0]
    base = base * lista[0]
print(f'{lista[0]} elevado por {expoente} = {tot}')
