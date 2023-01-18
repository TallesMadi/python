data = str(input('Informe a data de nascimento no estilo "dd/mm/aaaa": '))
mes = data[3] + data[4]
if mes == '01':
    mes = 'Janeiro'
elif mes == '02':
    mes = 'Fevereiro'
elif mes == '03':
    mes = 'Março'
elif mes == '04':
    mes = 'Abril'
elif mes == '05':
    mes = 'Maio'
elif mes == '06':
    mes = 'Junho'
elif mes == '07':
    mes = 'Julho'
elif mes == '08':
    mes = 'Agosto'
elif mes == '09':
    mes = 'Setembro'
elif mes == '10':
    mes = 'Outubro'
elif mes == '11':
    mes = 'Novembro'
else:
    mes = 'Dezembro'
print(f'Você nasceu no dia {data[0]+data[1]} de {mes} de {data[6] + data[7] + data[8] + data[9]}')