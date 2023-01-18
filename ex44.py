def conta_espacos(x):
    total = 0
    for c in range(0, len(x)):
        letra = x[c]
        if letra == ' ':
            total += 1
    return total


def conta_palavras(x):
    letra = ''
    for c in range(0, len(x)):
        letra += x[c]
    num = letra.split()
    num = len(num)      
    return num


def conta_caracteres(x):
    letra = ''
    for c in range(0, len(x)):
        letra += x[c]
    num = len(letra)      
    return num


def analize_letras(x):
    letra = ''
    lista = []
    for c in range(0, len(x)):
        letra += x[c]
    lista.append('Sequência do numéro de letras encontras na frase respectivamente de A até Z:')
    lista.append(letra.count('a'))
    lista.append(letra.count('b'))
    lista.append(letra.count('c'))
    lista.append(letra.count('d'))
    lista.append(letra.count('e'))
    lista.append(letra.count('f'))
    lista.append(letra.count('g'))
    lista.append(letra.count('h'))
    lista.append(letra.count('i'))
    lista.append(letra.count('j'))
    lista.append(letra.count('k'))
    lista.append(letra.count('l'))
    lista.append(letra.count('m'))
    lista.append(letra.count('n'))
    lista.append(letra.count('o'))
    lista.append(letra.count('p'))
    lista.append(letra.count('q'))
    lista.append(letra.count('r'))
    lista.append(letra.count('s'))
    lista.append(letra.count('t'))
    lista.append(letra.count('u'))
    lista.append(letra.count('v'))
    lista.append(letra.count('w'))
    lista.append(letra.count('x'))
    lista.append(letra.count('y'))
    lista.append(letra.count('z'))

    return lista 


def num_maiuscula(x):
    letra = ''
    maiuscula = 0
    for c in range(0, len(x)):
        letra += x[c]
    for i in range(0, len(letra)):
        alto = letra[i].isupper()
        if alto == True:
            maiuscula += 1
    return maiuscula
        

frase = 'Talles Madi Pinheiro Morette'
# print(conta_espacos(frase))
# print(conta_palavras(frase))
# print(conta_caracteres(frase))
# print(analize_letras(frase))
# print(num_maiuscula(frase))