from random import randint
from time import sleep

print('Sorteador de números Mega-Sena!')
qntd_jogos = int(input('Quantos jogos você quer? '))
for c in range(0, qntd_jogos):
    print(randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60))
    sleep(1)
    