var = open('c:/Users/talle/OneDrive/Documentos/python/ex47.txt', 'r')
arq = open('c:/Users/talle/OneDrive/Documentos/python/ex47_final.txt', 'w')
leitor = var.readlines()
linhas = list(range(len(leitor)))
for c in range(len(leitor)):
    linhas[c] = [leitor[c]]

inteiros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
numeros = []
variavel = ''
for c in range(len(linhas)):
    if c >= 1:
        numeros.append('fim')
    for i in range(len(linhas[c][0])):
        if i == (len(linhas[c][0])-1) and linhas[c][0][i] in inteiros:
            variavel += linhas[c][0][i]
            numeros.append(variavel)
            variavel = ''
        elif linhas[c][0][i] in inteiros:
            variavel += linhas[c][0][i]
        else:
            numeros.append(variavel)
            variavel = ''

indice = 0
final = [0]*(numeros.count('fim') + 1)
for c in range(len(numeros)):
    if numeros[c] == 'fim':
        indice += 1
    else:
        final[indice] += float(numeros[c])

media = [0]*(len(final))
for c in range(len(final)):
    media[c] = final[c] / 2

for c in range(len(final)):
    if c >= 1 and c < len(final):
        arq.writelines('\n')
    if media[c] >= 7:
        arq.writelines(f'APROVADO - Media: {media[c]}')
    else:
        arq.writelines(f'REPROVADO - Media: {media[c]}')

var.close()
arq.close()