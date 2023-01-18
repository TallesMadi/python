def multa():
    import datetime

    hora = datetime.datetime.now().hour
    print('Pesqueiro São Tomé das Águas Claras')
    nome = str(input('Informe seu nome: ')).capitalize()
    if hora >= 5 and hora < 12:
        print(f'Bom Dia, {nome}!')
    elif hora >= 12 and hora < 18:
        print(f'Boa Tarde, {nome}!')
    else:
        print(f'Boa Noite, {nome}!')
    peso = float(input('Informe quantos quilos de peixe você pescou: '))
    if peso <= 50:
        print(f'Você não excedeu o limite de 50 kg por pessoa na pesca, sendo assim não multado!')
    else:
        excesso = peso - 50
        multa = excesso * 4
        print(f'Você excedeu {excesso:.1f} Kg da máxima permitida, resultando numa multa de R$4.00 por kg a mais. \n Desta forma, sua multa foi de R${multa:.2f}')

multa()