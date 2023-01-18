def ver_data(x):
    lista = []
    var = ''
    for c in range(len(x)):
        # fazer uma lista com tres strings, tirando o '/', formando dia, mes e ano
        if x[c] == '/':
            lista.append(var)
            var = ''
        else:
            var += x[c]
    lista.append(var)
    dia = int(lista[0])
    mes = lista[1]
    ano = int(lista[2])
    if ano % 400 == 0 and ano % 4 == 0 and ano % 100 != 0:
        # verificação se o ano é bissexto ou não
        bissexto = True
    else: 
        bissexto = False 
    if ano > 0:
        # se o ano for maior que zero continua, senao para e retorna false
        if int(mes) >= 1 and int(mes) <= 12: 
            # se o mes estiver entre 1 e 12 continua, senao retorna false
            if dia >= 1 and dia <= 31:
                # se o dia estiver entre 1 e 31 continua, senao retorna false
                if bissexto == True:
                    # verificador para dias do ano bissexto
                    if str(mes) == '02' and dia <= 29:
                        return True
                    elif str(mes) == '01' and dia <= 31:
                        return True
                    elif str(mes) == '03' and dia <= 31:
                        return True
                    elif str(mes) == '04' and dia <= 30:
                        return True
                    elif str(mes) == '05' and dia <= 31:
                        return True
                    elif str(mes) == '06' and dia <= 30:
                        return True
                    elif str(mes) == '07' and dia <= 31:
                        return True
                    elif str(mes) == '08' and dia <= 31:
                        return True
                    elif str(mes) == '09' and dia <= 30:
                        return True
                    elif str(mes) == '10' and dia <= 31:
                        return True
                    elif str(mes) == '11' and dia <= 30:
                        return True
                    elif str(mes) == '12' and dia <= 31:
                        return True
                    else:
                        return False
                else:
                    # verificador para dias do ano normal
                    if str(mes) == '02' and dia <= 28:
                        return True
                    elif str(mes) == '01' and dia <= 31:
                        return True
                    elif str(mes) == '03' and dia <= 31:
                        return True
                    elif str(mes) == '04' and dia <= 30:
                        return True
                    elif str(mes) == '05' and dia <= 31:
                        return True
                    elif str(mes) == '06' and dia <= 30:
                        return True
                    elif str(mes) == '07' and dia <= 31:
                        return True
                    elif str(mes) == '08' and dia <= 31:
                        return True
                    elif str(mes) == '09' and dia <= 30:
                        return True
                    elif str(mes) == '10' and dia <= 31:
                        return True
                    elif str(mes) == '11' and dia <= 30:
                        return True
                    elif str(mes) == '12' and dia <= 31:
                        return True
                    else:
                        return False
            else: 
                return False
        else:
            return False
    else:
        return False

data = '12/02/2004'
print(ver_data(data))