print('Salto em Distância')
nome = str(input('Informe seu nome: ')).title()
lista = []
for c in range(1, 6):
    nota = float(input(f'Nota do {c}° salto: '))
    lista.append(nota)
lista.sort() 
menor = lista[0]
maior = lista[4]
lista.remove(lista[0])
lista.remove(lista[3])
media = (lista[0] + lista[1] + lista[2]) / 3
print(f'''Atleta: {nome}
Maior Salto: {maior}
Menor Salto: {menor}
Média: {media:.1f}''')
