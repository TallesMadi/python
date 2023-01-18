alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cripto = ''
indice = ''
frase = str(input('Digite uma frase qualquer: ')).lower().replace('à', 'a').replace('á', 'a').replace('ã', 'a').replace('ê', 'e').replace('é', 'e').replace('í', 'i').replace('ì', 'i').replace('ó', 'o').replace('ò', 'o').replace('ô', 'o').replace('õ', 'o').replace('ú', 'u').replace('ç', 'c')

while True:
    chave = int(input('Qual a chave que você deseja para a criptografia: (ex - chave 2: a = d, b = e... ) '))
    if chave >= 0 and chave <= 13:
        break
    else:
        print('Tente novamente!')
 
for c in range(len(frase)):
    if frase[c] in alfa:
        indice = alfa.index(frase[c])
        if indice >= (25 - chave):
            indice = (25 - indice) + (chave + 1)
            cripto += alfa[indice]
        else:
            cripto += alfa[indice + (chave + 1)]
    else:
        cripto += frase[c]
print(cripto)