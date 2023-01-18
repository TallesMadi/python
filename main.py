from random import choice
from time import sleep
print('{}Jokenpô{}'.format('\033[1;34m', '\033[m'))
while True:
    jogada = str(input('Vamos jogar Jokenpô! Escolha seu movimento (Pedra, Papel ou Tesoura): ')).capitalize()
    if jogada == 'Pedra' or jogada == 'Tesoura' or jogada == 'Papel':
        break
    else:
        print(f'A jogada {jogada} é inválida!')
lista = ['Pedra', 'Papel', 'Tesoura']
pc = choice(lista)
if jogada == 'Pedra' and pc == 'Tesoura' or jogada == 'Tesoura' and pc == 'Papel' or jogada == 'Papel' and pc == 'Pedra':
    print('{}{}{}'.format('\033[36m', jogada, '\033[m'))
    sleep(1)
    print('{}{}{}'.format('\033[35m', pc, '\033[m'))
    sleep(1)
    print('Você {}ganhou!{} {} vence {}!'.format('\033[1;32m', '\033[m', jogada, pc))
elif jogada == pc:
    print('{}{}{}'.format('\033[36m', jogada, '\033[m'))
    sleep(1)
    print('{}{}{}'.format('\033[35m', pc, '\033[m'))
    sleep(1)
    print('{}Empate!{} Fizemos a mesma jogada!'.format('\033[1;33m', '\033[m'))
else:
    print('{}{}{}'.format('\033[36m', jogada, '\033[m'))
    sleep(1)
    print('{}{}{}'.format('\033[35m', pc, '\033[m'))
    sleep(1)
    print('Você {}perdeu!{} {} vence {}!'.format('\033[1;31m', '\033[m', pc, jogada))