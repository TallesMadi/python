var = open('c:/Users/talle/OneDrive/Documentos/python/ex46.txt', 'r')
arq = open('c:/Users/talle/OneDrive/Documentos/python/ex46_final.txt', 'w')
leitor = var.readlines()
lista = list(range(len(leitor)))
inteiros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
numeros = []

for c in range(len(leitor)):
    lista[c] = leitor[c]

for c in range(len(lista)):
    lista[c] = [lista[c]]

variavel = ''
for c in range(len(lista)):
    if c >= 1:
        numeros.append('fim')
    for i in range(len(lista[c][0])):
        if i == (len(lista[c][0])-1) and lista[c][0][i] in inteiros:
            variavel += lista[c][0][i]
            numeros.append(variavel)
            variavel = ''
        elif lista[c][0][i] in inteiros:
            variavel += lista[c][0][i]
        else:
            numeros.append(variavel)
            variavel = ''

indice = 0
final = [0]*(numeros.count('fim') + 1)
for c in range(len(numeros)):
    if numeros[c] == 'fim':
        indice += 1
    else:
        final[indice] += int(numeros[c])

for c in range(len(final)):
    arq.writelines(str(final[c]))
    if c != (len(final) - 1):
        arq.writelines('\n')

var.close()
arq.close()