nome = str(input('Informe seu nome: ')).upper()
for c in range(len(nome)):
    print(nome[0:c + 1])


for i in range(len(nome), -1, -1):
    print(nome[0:i])
