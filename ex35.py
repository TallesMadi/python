nome = str(input('Escreva um texto criptografado: ')).lower()
cripto = ''
for c in range(len(nome)): 
    if nome[c] == 'd':
        cripto += 'a'
    elif nome[c] == 'e':
        cripto += 'b'
    elif nome[c] == 'f':
        cripto += 'c'
    elif nome[c] == 'g':
        cripto += 'd'
    elif nome[c] == 'h':
        cripto += 'e'
    elif nome[c] == 'i':
        cripto += 'f'
    elif nome[c] == 'j':
        cripto += 'g'
    elif nome[c] == 'k':
        cripto += 'h'
    elif nome[c] == 'l':
        cripto += 'i'
    elif nome[c] == 'm':
        cripto += 'j'
    elif nome[c] == 'n':
        cripto += 'k'
    elif nome[c] == 'o':
        cripto += 'l'
    elif nome[c] == 'p':
        cripto += 'm'
    elif nome[c] == 'q':
        cripto += 'n'
    elif nome[c] == 'r':
        cripto += 'o'
    elif nome[c] == 's':
        cripto += 'p'
    elif nome[c] == 't':
        cripto += 'q'
    elif nome[c] == 'u':
        cripto += 'r'
    elif nome[c] == 'v':
        cripto += 's'
    elif nome[c] == 'w':
        cripto += 't'
    elif nome[c] == 'x':
        cripto += 'u'
    elif nome[c] == 'y':
        cripto += 'v'
    elif nome[c] == 'z':
        cripto += 'w'
    elif nome[c] == 'a':
        cripto += 'x'
    elif nome[c] == 'b':
        cripto += 'y'
    elif nome[c] == 'c':
        cripto += 'z'
    else:
        cripto += nome[c]
print(cripto)