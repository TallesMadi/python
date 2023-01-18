print('Medidor de Pênis: Parâmetros Artimanhas')
medida = float(input('Informe o tamanho do seu pênis em centímetros: '))
if medida > 0 and medida < 6:
    print(f'Tá tudo bem com você? Porque {medida} cm não é normal não!')
elif medida >= 6 and medida <= 12:
    print(f'{medida} cm KKKK pipizin júnior!')
elif medida > 12 and medida < 17:
    print(f'{medida} cm, na média bro!')
elif medida >=17 and medida <= 20: 
    print(f'Você é um Deus com {medida} cm na calça!')
elif medida > 20:
    print('Para de mentir, seu arrombado!')
else:
    print(f'Acho que o valor {medida} está errado!')