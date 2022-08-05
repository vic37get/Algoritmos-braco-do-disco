import sys

arquivo = sys.stdin
dados = arquivo.readlines()

for index in range(0, len(dados)):
    dados[index] = int(dados[index])

qtd_cilindros = dados[0]
inicio = dados[1]
requisicoes = dados[2:]

def FCFS():
    movimentacoes = 0
    anterior = inicio
    for req in enumerate(requisicoes):
        if req > qtd_cilindros:
            print('Maior que o número de cilindros!')
        else:
            movimentacoes = movimentacoes + (abs(req - anterior))
            anterior = req
    return movimentacoes
    
print('FCFS: {}'.format(FCFS()))
