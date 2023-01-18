lista = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input('Informe um número: '))
        if lista[l][c] > maior:
            maior = lista[l][c]
        if l == 0 and c == 0:
            menor = lista[0][0]
        elif lista[l][c] < menor:
            menor = lista[l][c]
print(lista)
print(lista[0][0], lista[1][0], lista[2][0])
print(maior)
print(menor)