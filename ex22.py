from time import sleep
from random import randint

print('''\033[1;34mJogo: Par ou Ímpar\033[m
Neste jogo você deve escolher um número de 0 a 9, e escolher uma categoria: par ou ímpar. 
Desta forma, o computador também escolherá um número e ficará com a outra categoria, 
disputando para ver se a soma dos números escolhidos foi da sua categoria!
\033[1;36mBoa sorte!\033[m''')

sleep(1)

vezes = int(input('Informe quantas vezes gostaria de jogar: '))
for c in range(0, vezes):
    while True:
        par_ou_impar = str(input('Escolha: Par ou Ímpar? ')).replace('i', 'í').replace('I', 'Í').capitalize()
        if par_ou_impar == 'Par':
            while True:
                numero = int(input('Você é Par! Escolha um número inteiro de 0 a 9: '))
                if numero >= 0 and numero <= 9:
                    break
                else:
                    print(f'O número {numero}, não é permitido, tente um número de 0 a 9!')
            numero_pc = randint(0, 9)
            soma = numero + numero_pc
            if soma % 2 == 0:
                print(f'O seu número escolhido foi {numero} e o pc escolheu {numero_pc}.')
                sleep(1)
                print(f'Desta forma, a soma deles deu {soma}, sendo par!')
                print(f'\033[1;32mVocê Venceu!\033[m')
                break
            else:
                print(f'O seu número escolhido foi {numero} e o pc escolheu {numero_pc}.')
                sleep(1)
                print(f'Desta forma, a soma deles deu {soma}, sendo ímpar!')
                print(f'\033[1;31mVocê Perdeu!\033[m')
                break

        elif par_ou_impar == 'Ímpar':
            while True:
                numero = int(input('Você é Ímpar! Escolha um número inteiro de 0 a 9: '))
                if numero >= 0 and numero <= 9:
                    break
                else:
                    print(f'O número {numero}, não é permitido, tente um número de 0 a 9!')
            numero_pc = randint(0, 9)
            soma = numero + numero_pc
            if soma % 2 == 0:
                print(f'O seu número escolhido foi {numero} e o pc escolheu {numero_pc}.')
                sleep(1)
                print(f'Desta forma, a soma deles deu {soma}, sendo par!')
                print(f'\033[1;31mVocê Perdeu!\033[m')
                break
            else:
                print(f'O seu número escolhido foi {numero} e o pc escolheu {numero_pc}.')
                sleep(1)
                print(f'Desta forma, a soma deles deu {soma}, sendo ímpar!')
                print(f'\033[1;32mVocê Venceu!\033[m')
                break

        else:
            print(f'O valor "{par_ou_impar}" inserido está incorreto! Tente novamente!') 

