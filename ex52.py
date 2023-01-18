import json, random, math

ler = open('C:/Users/talle/OneDrive/Documentos/python/json3.json', 'r')
arq = open('C:/Users/talle/OneDrive/Documentos/python/json2.json', 'w')

leitor = [json.load(ler)]
n = 0
obj = leitor[0]

def cadastrar():
    h = 0
    while h != 'Sim':
        id = random.randint(000000, 999999)
        for c in range(len(obj)):
            if id != obj[c]["id"]: 
                h = 'Sim'
    nome = str(input('Informe o nome: ')).capitalize()
    telefone = int(input('Informe seu telefone (ex: 999999999): '))
    peso = int(input('Informe seu peso: '))
    altura = int(input('Informe sua altura: '))
    sexo = str(input('Informe seu sexo (ex: F ou M): ')).upper()
    mensalidade = random.choice([669.90, 559.90, 769.90, 334.90, 899.90, 999.90])
    obj.append({"id": id, "nome": nome, "telefone": telefone, "peso": peso, "altura": altura, "mensalidade": mensalidade,  "sexo": sexo})
    return (f'O id será {id} e a mensalidade será de R${mensalidade}')
    
def lista():
    lista_nome = []
    for c in range(len(obj)):
        lista_nome.append(obj[c]["nome"])
    return(lista_nome)

def id():
    id = int(input('Escreva o id do aluno (ex: 000000): '))
    c = 0
    if id == obj[c]["id"]:
        while True:
            if obj[c]["id"] == id:
                num = c
                break
            else:
                c += 1
        return(f'''
    id: {obj[num]["id"]}
    Nome: {obj[num]["nome"]}
    Telefone: {obj[num]["telefone"]}
    Peso: {obj[num]["peso"]} Kg
    Altura: {obj[num]["altura"]} cm
    Sexo: {obj[num]["sexo"]}
    Mensalidade: R${obj[num]["mensalidade"]}''')
    else:
        return(f'id {id} não encontrado')

def imc():
    imc_l = []
    nome_l = []
    for c in range(len(obj)):
        imc = obj[c]["peso"] / ((obj[c]["altura"] / 100) ** 2)
        if imc > 30:
            nome_l.append(obj[c]["nome"])
            imc_l.append(math.ceil(imc))
    return (nome_l, imc_l)

def sair():
    json.dump(obj, arq)
    return 'Até mais!'
