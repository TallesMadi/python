var = open('c:/Users/talle/OneDrive/Documentos/python/ex43.txt', 'r')
arq = open('c:/Users/talle/OneDrive/Documentos/python/ex43_final.txt', 'w')

leitor = var.read()
total = 0
linhas = leitor.split("\n")
num = list(range(len(leitor)))
number = []
for c in linhas:
    if c:
        total += 1

for c in range(len(leitor)):
    num[c] = leitor[c]

while True:
    if "\n" in num:
        num.remove("\n")
    else:
        break

vezes = 0
variavel = ''
for c in range(len(num)):
    variavel += num[c]
    vezes += 1
    if vezes == 2:
        number.append(int(variavel))
        vezes = 0
        variavel = ''

soma = sum(number)
media = soma / int(total)

arq.writelines('Soma:')
arq.writelines('\n')
arq.writelines(str(soma))
arq.writelines('\n')
arq.writelines('Media:')
arq.writelines('\n')
arq.writelines(str(media))

var.close()
arq.close()