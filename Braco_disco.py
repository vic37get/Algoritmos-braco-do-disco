import sys

import numpy as np

arquivo = sys.stdin
dados = arquivo.readlines()

for index in range(0, len(dados)):
    dados[index] = int(dados[index])

qtd_cilindros = dados[0]
inicio = dados[1]
requisicoes = dados[2:]

def FCFS(requisicoes, inicio):
    movimentacoes = 0
    anterior = inicio
    for req in requisicoes:
        if req < qtd_cilindros:
            movimentacoes = movimentacoes + (abs(req - anterior))
            anterior = req   
        else:
            print('Maior que o número de cilindros!')
    return movimentacoes

def SSTF(requisicoes, inicio):
    requisicoes = np.asarray(requisicoes)
    movimentacoes = 0
    anterior = inicio
    for req in requisicoes:
        if req < qtd_cilindros:
            index = (np.abs(requisicoes - anterior)).argmin()
            menor = requisicoes[index]
            movimentacoes = movimentacoes + (abs(menor - anterior))
            anterior = menor
            requisicoes = np.delete(requisicoes, index)
        else:
            print('Requisição maior que a capacidade do disco!')
            requisicoes = np.delete(requisicoes, index)
    return movimentacoes

def ELEVADOR(requisicoes, inicio):  
    movimentacoes = 0
    anterior = inicio
    reqOutraDir = []
    requisicoes = sorted(requisicoes)
    for req in requisicoes:
        if req < qtd_cilindros:
            if req > inicio:
                movimentacoes = movimentacoes + (abs(req - anterior))
                anterior = req
            else:
                reqOutraDir.append(req)
        else:
            print('Requisição maior que a capacidade do disco!')
    reqOutraDir = sorted(reqOutraDir, reverse=True)
    for req in reqOutraDir:
        movimentacoes = movimentacoes + (abs(req - anterior))
        anterior = req
    return movimentacoes

print('FCFS: {}'.format(FCFS(requisicoes, inicio)))
print('SSTF: {}'.format(SSTF(requisicoes, inicio)))
print('ELEVADOR: {}'.format(ELEVADOR(requisicoes, inicio)))
