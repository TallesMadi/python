nome = str(input('Informe seu nome: ')).title()
sal = float(input('Informe seu salário bruto: '))
dependentes = int(input('Informe o número de dependentes: '))
salmin = int(input('Informe o número de salários minimos que você ganha por mês: '))
if salmin <= 3:
    fgts = 0.08 * 1212
    inss = 0.05 * 1212
elif salmin > 3 and salmin <= 6:
    fgts = 0.085 * 1212
    inss = 0.06 * 1212
else:
    fgts = 0.09 * 1212
    inss = 0.07 * 1212
sal_fam =(0.05 * dependentes) * sal
sal_liq = (sal + sal_fam) - (fgts + inss)
print(f'''Sr(a). {nome}
FGTS: R${fgts:.2f}
INSS: R${inss:.2f}
Salário Família: R${sal_fam:.2f}
Salário Líquido: R${sal_liq:.2f}''')
