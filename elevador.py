#Tratamento da entrada de dados
def TratamentoArquivo(arquivo):
    for index in range(0, len(arquivo)):
        arquivo[index] = int(arquivo[index])
    return arquivo

def ELEVADOR(arquivo):
    print('\n---Algoritmo do Elevador---\n')
    dados = TratamentoArquivo(arquivo)
    inicio = dados[1]
    qtd_cilindros = dados[0]
    requisicoes = dados[2:]
    movimentacoes = 0
    anterior = inicio
    #Requisições na direção oposta a inicial
    reqOutraDir = []
    requisicoes = sorted(requisicoes)

    for req in requisicoes:
        print('Requisições:\n',requisicoes)
        print('Cilindro atual: ', anterior)
        #Se a requisição atual não for maior que a quantidade de cilindros
        if req < qtd_cilindros:
            #Se a requisição atual for maior que a requisição inicial
            if req > inicio:
                print('Requisição escolhida: ', req)
                movimentacoes = movimentacoes + (abs(req - anterior))
                anterior = req
                print('Movimentações: ', movimentacoes)
            #Se a requisição atual for na direção oposta a requisição inicial
            else:
                #Adiciona 
                reqOutraDir.append(req)
        else:
            print('Requisição maior que a capacidade do disco!')
        print('\n************************************************************\n')
    #Ordenando as requisições da direção oposta ao inicio de forma decrescente        
    reqOutraDir = sorted(reqOutraDir, reverse=True)
    #Realizando as requisições na direção oposta a inicial
    for req in reqOutraDir:
        print('Requisições:\n', reqOutraDir)
        print('Cilindro atual: ', anterior)
        print('Requisição escolhida: ', req)
        movimentacoes = movimentacoes + (abs(req - anterior))
        print('Movimentações: ', movimentacoes)
        anterior = req
        print('\n************************************************************\n')

    return movimentacoes
