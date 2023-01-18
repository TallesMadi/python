var = open('c:/Users/talle/OneDrive/Documentos/python/ex48.txt', 'r')
arq = open('c:/Users/talle/OneDrive/Documentos/python/ex48_final.txt', 'w')

leitor = var.readlines()
lista = list(range(len(leitor)))
for c in range(len(leitor)):
    lista[c] = [leitor[c]]

# letra = str(input('Escolha uma letra para ver quantas vezes ela aparece no poema: '))

alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letras = []
for c in range(len(lista)):
    for i in range(len(lista[c])):
        for f in range(len(lista[c][i])):
            if lista[c][i][f] in alfa:
                letras.append(lista[c][i][f])
while True:
    letra = str(input('Escolha uma letra para ver quantas dela existem no poema: ')).lower()
    if letra in alfa:
        break
    else:
        print('Valor inserido inválido. Tente novamente!')
letra_b = letra.upper

arq.writelines(f'Total de letras {letra.upper()} no poema: ')
arq.writelines(f'\n{str(letras.count(letra) + letras.count(letra_b))}')

var.close()
arq.close()