lista = []
nome = str(input('Informe seu nome: ')).title()
for c in range(1, 8):
    nota = float(input(f'Informe a nota do {c}° jurado: '))
    lista.append(nota)
lista.sort()
menor = lista[0]
maior = lista[6]
lista.remove(lista[0])
lista.remove(lista[5])
media = (lista[0] + lista[1] + lista[2] + lista[3] + lista[4]) / 5
print(f'''RESULTADO FINAL:
Atleta: {nome};
Melhor nota: {maior};
Pior nota: {menor};
Média de notas: {media:.1f}''')
