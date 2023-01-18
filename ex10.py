print('\a Calculadora IMC: Índice de Massa Corporal')
peso = float(input('Informe seu peso em kg: '))
altura = float(input('Informe sua altura em metros: '))
imc = peso / (altura ** 2)
if imc < 18.5 and imc > 0:
    print(f'IMC = {imc:.1f} \n Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print(f'IMC = {imc:.1f} \n Peso Normal')
elif imc >= 25 and imc < 30:
    print(f'IMC = {imc:.1f} \n Sobrepeso')
elif imc >= 30 and imc < 35:
    print(f'IMC = {imc:.1f} \n Obesidade Grau I')
elif imc >= 35 and imc < 40:
    print(f'IMC = {imc:.1f} \n Obesidade Grau II')
elif imc >= 40:
    print(f'IMC = {imc:.1f} \n Obesidade Grau III ou Mórbida')
else:
    print(f'O valor {peso} ou {altura} estão incorretos!')
