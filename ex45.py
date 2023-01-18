import ex44

var = open('c:/Users/talle/OneDrive/Documentos/python/ex45.txt', 'r')
arq = open('c:/Users/talle/OneDrive/Documentos/python/ex45_final.txt', 'w')
linhas = var.read()
total = 0
tot_l = linhas.split("\n")   
for i in tot_l: 
    if i: 
        total += 1

num_palavra = str(ex44.conta_palavras(linhas))
num_espaco = str(ex44.conta_espacos(linhas))
num_caract = str(ex44.conta_caracteres(linhas))
arq.writelines('Numero de palavras: ')
arq.writelines(num_palavra)
arq.writelines('\nNumero de espacos: ')
arq.writelines(num_espaco)
arq.writelines('\nNumero de caracteres: ')
arq.writelines(num_caract)
arq.writelines('\nNumero de linhas: ')
arq.writelines(str(total))
var.close()
arq.close()