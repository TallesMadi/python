def alt():
    print('Peso Ideal baseado na altura!')
    altura = float(input('Informe a sua altura em metros: '))
    while True:
        sexo = str(input('Informe seu sexo: ')).capitalize()
        if sexo == 'Masculino' or sexo == 'Feminino':
            break
        else:
            print(f'O sexo {sexo} está incorreto. Tente inserir "Masculino" ou "Feminino"')
    if sexo == 'Masculino':
        peso_ideal = (72.7 * altura) - 58
        print(f'O seu peso ideal é de {peso_ideal:.1f} Kg!')
    else:
        peso_ideal = (62.1 * altura) - 44.7
        print(f'O seu peso ideal é de {peso_ideal:.1f} Kg!')
alt()
    