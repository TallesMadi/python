print('\033[1;34m Temperatura: Celsius e Fahrenheit \033[m')
res = int(input('Qual a escala da temperatura inicial (Celsius = 1; Fahrenheit = 2)? '))
if res == 1:
    temp_inicial = float(input('Informe a temperatura em graus Celsius: '))
    temp_final = (temp_inicial * 9 / 5) + 32
    print(f'{temp_inicial:.1f}°F é igual a {temp_final:.1f}°C')
elif res == 2:
    temp_inicial = float(input('Informe a temperatura em graus Farenheit: '))
    temp_final = 5 * ((temp_inicial - 32) / 9 )
    print(f'{temp_inicial:.1f}°C é igual a {temp_final:.1f}°F')
else:
    print(f'O valor {res} inserido está incorreto. Digite 1 ou 2 no campo.')