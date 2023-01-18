from time import sleep

print('Verificador de Par ou Ímpar!')
sleep(1)
while True:
    numero = int(input('Informe um número inteiro: '))
    if numero % 2 == 0:
        print(f'O número \033[1;34m{numero}\033[m é par!')
    else:
        print(f'O número \033[1;31m{numero}\033[m é ímpar!')
    continuar = str(input('Quer continuar? (S ou N) ')).upper()
    if continuar == 'N':
        print('Até mais!')
        break
    elif continuar == 'S':
        print('Então vamos lá!')
