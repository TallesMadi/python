from time import sleep
from random import choice
print('Jogo: Masmorras!')
print('Você encontrou um monstro, precisa derrotá-lo!')
boss = 1000
personagem = 350
mana = 120
while True:
    golpe = int(input('[1] Ataque normal (10 de mana) \n[2] Ataque pesado (35 de mana) \n[3] Defender (10 de mana) '
                      '\n[4] Procurar itens (10 de mana) \nEscolha um ataque: '))
    escolha = ['Mana', 'Vida', 'Nada']
    sorte = choice(escolha)
    if golpe == 1:
        boss -= 100
        personagem -= 50
        mana -= 10
        print('\o/______/ÒÓ\ ')
        sleep(1)
        print('\o/_/ÒÓ\ ')
        sleep(1)
        print(f'Vida do boss: {boss}HP---Sua vida: {personagem}HP---Mana: {mana}')
        sleep(1)
    if golpe == 2:
        boss -= 250
        personagem -= 50
        mana -= 35
        print('\o/______/ÒÓ\ ')
        sleep(1)
        print('\o/_*/ÒÓ\* ')
        sleep(1)
        print(f'Vida do boss: {boss}HP---Sua vida: {personagem}HP---Mana: {mana}')
        sleep(1)
    if golpe == 3:
        mana -= 10
        personagem += 10
        print('\o/______/ÒÓ\ ')
        sleep(1)
        print('(\o/)_/ÒÓ\ ')
        sleep(1)
        print(f'Vida do boss: {boss}HP---Sua vida: {personagem}HP---Mana: {mana}')
        sleep(1)
    if golpe == 4:
        print('PROCURANDO...')
        sleep(1)
        if sorte == 'Mana':
            mana += 100
            print('Mana encontrado (+100 de mana)')
        if sorte == 'Vida':
            personagem += 150
            print('Poção encontrada (+150 de vida)')
        if sorte == 'Nada':
            print('Nada encontrado')
    if boss <= 0:
        print('Parabéns! Você derrotou o boss!')
        break
    if personagem <= 0:
        print('GAME OVER! Você acabou morrendo para o boss!')
        break
    if mana <= 0:
        print('GAME OVER! Sua mana acabou!')
print('FIM!')