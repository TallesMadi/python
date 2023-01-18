def salario():
    import datetime

    print('Informe Salarial')
    hora = datetime.datetime.today().hour
    nome = str(input('Informe seu nome: ')).title()
    if hora >= 5 and hora < 12:
        print(f'Bom Dia, {nome}!')
    if hora >= 12 and hora < 18:
        print(f'Boa Tarde, {nome}!')
    else:
        print(f'Boa Noite, {nome}!')
    hora_pag = float(input(f'{nome}, quanto você recebe por hora trabalhada? '))
    hora_trab = int(input('Quantas horas você trabalha durante todo o mês? '))
    salario_bruto = hora_pag * hora_trab
    ir = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - (ir + inss + sindicato)
    print(f'\nSalário Bruto: R${salario_bruto:.2f} \nDescontos: \nImposto de Renda: R${ir:.2f} \nINSS: R${inss:.2f} \nSindicato: R${sindicato:.2f} \nFinal:\nSalário Liquido: R${salario_liquido:.2f}')

salario()