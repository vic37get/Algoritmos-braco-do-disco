import sys

import numpy as np

arquivo = sys.stdin
dados = arquivo.readlines()

for index in range(0, len(dados)):
    dados[index] = int(dados[index])

qtd_cilindros = dados[0]
inicio = dados[1]
requisicoes = dados[2:]

def FCFS(requisicoes):
    movimentacoes = 0
    anterior = inicio
    for req in requisicoes:
        if req > qtd_cilindros:
            print('Maior que o número de cilindros!')
        else:
            movimentacoes = movimentacoes + (abs(req - anterior))
            anterior = req
    return movimentacoes

def SSTF(requisicoes):
    requisicoes = np.asarray(requisicoes)
    movimentacoes = 0
    anterior = inicio
    for req in range(0, len(requisicoes)):
        index = (np.abs(requisicoes - anterior)).argmin()
        menor = requisicoes[index]
        movimentacoes = movimentacoes + (abs(menor - anterior))
        anterior = menor
        requisicoes = np.delete(requisicoes, index)
    return movimentacoes

def ELEVADOR(requisicoes):
    movimentacoes = 0



    return movimentacoes


print('FCFS: {}'.format(FCFS(requisicoes)))
print('SSTF: {}'.format(SSTF(requisicoes)))
