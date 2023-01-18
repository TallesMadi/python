print('Média Aritimética!')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media >= 0 and media < 7:
    print(f'REPROVADO! Sua média foi de {media:.2f}!')
elif media >= 7 and media <= 8:
    print(f'APROVADO! Sua média foi de {media:.2f}!')
elif media > 8 and media <= 10:
    print(f'PARABÉNS! Você foi aprovado com {media:.2f} de média!')
else:
    print(f'O valor {n1} ou o valor {n2} estão incorretos!')
