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

MOVIMENTACOES_FCFS = fc.FCFS(dados)
MOVIMENTACOES_SSTF = sst.SSTF(dados)
MOVIMENTACOES_ELEVADOR = elev.ELEVADOR(dados)

print('FCFS: {}'.format(MOVIMENTACOES_FCFS))
print('SSTF: {}'.format(MOVIMENTACOES_SSTF))
print('ELEVADOR: {}'.format(MOVIMENTACOES_ELEVADOR))
