print('Verificador de número primo')
num = int(input('Informe o seu número: '))
if num % num == 0 and num % 1 == 0 and num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0: 
    print(f'{num} é um número primo!') 
elif num == 2 or num == 3 or num == 5 or num == 7:
    print(f'{num} é um número primo!')
else: 
    print(f'{num} não é um número primo!')
