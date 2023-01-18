tam = int(input('Informe o tamanho do arquivo em MB: '))
vel = int(input('Informe a velocidade da Internet em Mbps: '))
tempo = tam / vel
print(f'Para instalar um arquivo de {tam}MB é necessário {tempo} segundos para concluir o download!')