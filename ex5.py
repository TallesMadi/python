print('Reajuste Salarial!')
sal = float(input('Informe seu salário em Reais: '))
if sal < 500 and sal > 0:
    reajuste1 = sal * 1.15
    print(f'Seu salário de R${sal:.2f} agora é de {reajuste1:.2f} com um reajuste de 15%.')
elif sal >= 500 and sal <= 1000:
    reajuste2 = sal * 1.1
    print(f'Seu salário de R${sal:.2f} agora é de {reajuste2:.2f} com um reajuste de 10%.')
elif sal > 1000:
    reajuste3 = sal * 1.05
    print(f'Seu salário de R${sal:.2f} agora é de {reajuste3:.2f} com um reajuste de 5%.')
else:
    print(f'O valor inserido "{sal}" está incorreto!')