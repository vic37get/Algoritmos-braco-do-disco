import numpy as np


#Tratamento da entrada de dados
def TratamentoArquivo(arquivo):
    for index in range(0, len(arquivo)):
        arquivo[index] = int(arquivo[index])
    return arquivo

def FCFS(arquivo):
    print('\n---Algoritmo do FCFS---\n')
    dados = TratamentoArquivo(arquivo)
    qtd_cilindros = dados[0]
    inicio = dados[1]
    requisicoes = np.asarray(dados[2:])
    movimentacoes = 0
    anterior = inicio

    for req in requisicoes:
        print('Requisições:\n',requisicoes)
        print('Cilindro atual: ', anterior)
        #Se a requisição atual não for maior que a quantidade total de cilindros
        if req < qtd_cilindros:
            print('Requisição escolhida: ', req)
            #Calculo das movimentações
            movimentacoes = movimentacoes + (abs(req - anterior))
            print('Movimentações: ', movimentacoes)
            anterior = req
        else:
            print('Maior que o número de cilindros!')
        print('\n************************************************************\n')

    return movimentacoes
