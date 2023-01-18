import ex50

n = 0
while n != 5:
        n = int(input('''\nSysAcademy
        Escolha a opção desejada:
        1 - Cadastrar novo aluno
        2 - Imprimir lista de alunos
        3 - Buscar aluno por id
        4 - Filtrar alunos com IMC > 30
        5 - Sair
        Opção: '''))

        if n == 1:
            print(ex50.cadastrar())
        elif n == 2:
            for c in range(len(ex50.lista())):
                print(ex50.lista()[c])
        elif n == 3:
            print(ex50.id())
        elif n == 4:
            for c in range(len(ex50.imc()[0])):
                print(ex50.imc()[0][c])
                print(ex50.imc()[1][c])
        elif n == 5:
            print(ex50.sair())
        else:
            print('Valor inserido incorreto!')