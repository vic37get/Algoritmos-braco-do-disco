import numpy as np


def TratamentoArquivo(arquivo):
    for index in range(0, len(arquivo)):
        arquivo[index] = int(arquivo[index])
    return arquivo

def SSTF(arquivo):
    dados = TratamentoArquivo(arquivo)
    requisicoes = np.asarray(dados[2:])
    qtd_cilindros = dados[0]
    inicio = dados[1]
    movimentacoes = 0
    anterior = inicio

    for req in requisicoes:
        #Se a requisição atual não for maior que a quantidade de cilindros.
        if req < qtd_cilindros:
            #Indice do vizinho mais próximo
            index = (np.abs(requisicoes - anterior)).argmin()
            #Vizinho mais próximo
            menor = requisicoes[index]
            #Calculo de movimentações
            movimentacoes = movimentacoes + (abs(menor - anterior))
            anterior = menor
            #Removendo a requisição já atendida da lista
            requisicoes = np.delete(requisicoes, index)
        #Numero maior que a quantidade de cilindros
        else:
            requisicoes = np.delete(requisicoes, index)
    return movimentacoes

#Passo a passo
def SSTFPassoApasso(arquivo):
    print('\n---Algoritmo do SSTF---\n')
    dados = TratamentoArquivo(arquivo)
    requisicoes = np.asarray(dados[2:])
    qtd_cilindros = dados[0]
    inicio = dados[1]
    movimentacoes = 0
    anterior = inicio

    for req in requisicoes:
        #Se a requisição atual não for maior que a quantidade de cilindros.
        print('Requisições:\n',requisicoes)
        print('Cilindro atual: ', anterior)
        if req < qtd_cilindros:
            #Indice do vizinho mais próximo
            index = (np.abs(requisicoes - anterior)).argmin()
            #Vizinho mais próximo
            menor = requisicoes[index]
            print('Requisição escolhida: ', menor)
            #Calculo de movimentações
            movimentacoes = movimentacoes + (abs(menor - anterior))
            anterior = menor
            print('Movimentações: ', movimentacoes)
            #Removendo a requisição já atendida da lista
            requisicoes = np.delete(requisicoes, index)
        else:
            print('Requisição maior que a capacidade do disco!')
            requisicoes = np.delete(requisicoes, index)
        print('\n************************************************************\n')
    return movimentacoes
