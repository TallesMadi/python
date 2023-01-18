import json, random, math

ler = open('C:/Users/talle/OneDrive/Documentos/python/json.json', 'r')
arq = open('C:/Users/talle/OneDrive/Documentos/python/json2.json', 'w')

obj = json.load(ler)
n = 0

def cadastrar():
    while True:
        id = random.randint(000000, 999999)
        if str(id) not in obj["id"]: 
            break
    nome = str(input('Informe o nome: ')).capitalize()
    telefone = str(input('Informe seu telefone (ex: 999999999): '))
    peso = str(input('Informe seu peso: '))
    altura = str(input('Informe sua altura: '))
    sexo = str(input('Informe seu sexo (ex: F ou M): ')).upper()
    mensalidade = random.choice([667, 559, 767, 334, 900, 1000])
    obj["nome"] += [nome]
    obj["id"] += [str(id)]
    obj["telefone"] += [telefone]
    obj["peso"] += [peso]
    obj["altura"] += [altura]
    obj["sexo"] += [sexo]
    obj["mensalidade"] += [str(mensalidade)]
    return (f'O id será {id} e a mensalidade será de R${mensalidade}')
    
def lista():
    return(obj["nome"])

def id():
    id = str(input('Escreva o id do aluno (ex: 000000): '))
    c = 0
    if id in obj["id"]:
        while True:
            if obj["id"][c] == id:
                num = c
                break
            else:
                c += 1
        return(f'''
    id: {obj["id"][num]}
    Nome: {obj["nome"][num]}
    Telefone: {obj["telefone"][num]}
    Peso: {obj["peso"][num]} Kg
    Altura: {obj["altura"][num]} cm
    Sexo: {obj["sexo"][num]}
    Mensalidade: R${obj["mensalidade"][num]}''')
    else:
        return(f'id {id} não encontrado')

def imc():
    imc_l = []
    nome_l = []
    for c in range(len(obj["peso"])):
        imc = int(obj["peso"][c]) / ((int(obj["altura"][c]) / 100) ** 2)
        if imc > 30:
            nome_l.append(obj["nome"][c])
            imc_l.append(math.ceil(imc))
    return (nome_l, imc_l)

def sair():
    json.dump(obj, arq)
    return 'Até mais!'
