print('Sequência de Números Primos')
tot = 0
lista = []
while True:
    # Esse while irá servir para repetir o programa até o usuário colocar o valor correto
    num = int(input('Digite até qual número você quer verificar os primos: '))
    if num < 2:
        print('Não existe número primo menor que 2!')
    elif num == 2:
        print('Só há o número 2 primo!')
    else:
        for c in range(2, num + 1):
            # Esse for será usado para repetir o programa abaixo num vezes
            tot = 0
            for n in range(1, num + 1):
                if c % n == 0:
                    # Irá verificar se o número é divisível por 2 números, se a variável tot for maior que 2, será desconsiderada
                    tot += 1
            if tot == 2:
                print(f'{c} é um número primo')
                # Se a variável tot for igual a 2, o número correspondente será primo
                lista.append(c)
        break
print(f'Sendo um total de {len(lista)} de números primos de 2 até {num}.')
