str1 = str(input('Escreve uma string: '))
str2 = str(input('Escreva outra string: '))
print(f'''Tamanho da String 1: {len(str1)}
Tamanho da String 2: {len(str2)}''')
if len(str1) != len(str2):
    print('As duas strings possuem tamanhos distintos!')
else: 
    print('As duas strings possuem o mesmo tamanho!')
if str1 == str2:
    print('As duas strings possuem o mesmo conteúdo!')
else:
    print('As strings possuem conteúdos distintos!')
