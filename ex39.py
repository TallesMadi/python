nome = str(input('Insira seu nome: ')).upper()
lista = []
for c in range(len(nome)):
    lista.append(nome[c])

lista.reverse()
print('Seu nome ao contrário é: ')
for i in range(len(lista)):
    print(lista[i], end='')