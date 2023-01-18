nome = str(input('Escreva um texto: ')).lower().replace('à', 'a').replace('á', 'a').replace('ã', 'a').replace('ê', 'e').replace('é', 'e').replace('í', 'i').replace('ì', 'i').replace('ó', 'o').replace('ò', 'o').replace('ô', 'o').replace('õ', 'o').replace('ú', 'u').replace('ç', 'c')
cripto = ''
for c in range(len(nome)): 
    if nome[c] == 'a':
        cripto += 'd'
    elif nome[c] == 'b':
        cripto += 'e'
    elif nome[c] == 'c':
        cripto += 'f'
    elif nome[c] == 'd':
        cripto += 'g'
    elif nome[c] == 'e':
        cripto += 'h'
    elif nome[c] == 'f':
        cripto += 'i'
    elif nome[c] == 'g':
        cripto += 'j'
    elif nome[c] == 'h':
        cripto += 'k'
    elif nome[c] == 'i':
        cripto += 'l'
    elif nome[c] == 'j':
        cripto += 'm'
    elif nome[c] == 'k':
        cripto += 'n'
    elif nome[c] == 'l':
        cripto += 'o'
    elif nome[c] == 'm':
        cripto += 'p'
    elif nome[c] == 'n':
        cripto += 'q'
    elif nome[c] == 'o':
        cripto += 'r'
    elif nome[c] == 'p':
        cripto += 's'
    elif nome[c] == 'q':
        cripto += 't'
    elif nome[c] == 'r':
        cripto += 'u'
    elif nome[c] == 's':
        cripto += 'v'
    elif nome[c] == 't':
        cripto += 'w'
    elif nome[c] == 'u':
        cripto += 'x'
    elif nome[c] == 'v':
        cripto += 'y'
    elif nome[c] == 'w':
        cripto += 'z'
    elif nome[c] == 'x':
        cripto += 'a'
    elif nome[c] == 'y':
        cripto += 'b'
    elif nome[c] == 'z':
        cripto += 'c'
    else:
        cripto += nome[c]
print(cripto)