def listsum(numList):
    if len(numList) == 1:
        print(numList)
        return numList[0]
    else:
        print(numList)
        return numList[0] + listsum(numList[1:])

print(listsum([1, 2, 3, 4, 5]))


def fatorial(x):
    if x <= 1:
        return 1
    else:
        return x * fatorial(x-1)
    
n = int(input('Escolha um número para calcular o fatorial: '))
print(fatorial(n))

def fatorial(x):
    soma = 1
    while True:
        if x == 0:
            break
        else:
            soma += soma * x
        x -= 1
    return soma

n = int(input('Escolha um número para calcular o fatorial: '))
print(fatorial(n))