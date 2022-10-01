import sys

import elevador as elev
import FCFS as fc
import SSTF as sst


def OpenFile():
    arquivo = sys.stdin
    try:
        dados = arquivo.readlines()
        return dados
    except:
        print('Arquivo não encontrado!')
        exit(0)

dados = OpenFile()

# Execução padrão
def Execução():
    MOVIMENTACOES_FCFS = fc.FCFS(dados)
    MOVIMENTACOES_SSTF = sst.SSTF(dados)
    MOVIMENTACOES_ELEVADOR = elev.ELEVADOR(dados)

    print('FCFS: {}'.format(MOVIMENTACOES_FCFS))
    print('SSTF: {}'.format(MOVIMENTACOES_SSTF))
    print('ELEVADOR: {}'.format(MOVIMENTACOES_ELEVADOR))

# Execução passo a passo
def ExecuçãoPassoApasso():
    MOVIMENTACOES_FCFS = fc.FCFSPassoApasso(dados)
    MOVIMENTACOES_SSTF = sst.SSTFPassoApasso(dados)
    MOVIMENTACOES_ELEVADOR = elev.ELEVADORPassoApasso(dados)

    print('FCFS: {}'.format(MOVIMENTACOES_FCFS))
    print('SSTF: {}'.format(MOVIMENTACOES_SSTF))
    print('ELEVADOR: {}'.format(MOVIMENTACOES_ELEVADOR))

#############################
#Execução do "main"
Execução()
#ExecuçãoPassoApasso()


