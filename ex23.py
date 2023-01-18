print('Verificador de Triângulos')
lado1 = float(input('Informe o 1° lado: '))
lado2 = float(input('Informe o 2° lado: '))
lado3 = float(input('Informe o 3° lado: '))
if lado1 == lado2 and lado1 == lado3:
    print('É um triângulo equilátero!')
elif lado1 != lado2 and lado1 != lado3:
    print('É um triângulo escaleno!')
else:
    print('É um triângulo isosceles!')
