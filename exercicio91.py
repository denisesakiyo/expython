from random import randint
from operator import itemgetter
from time import sleep

dados = {}
print('VALORES SORTEADOS')
ranking = []
for pos in range(1,5):
       dados[f"Jogador{pos}"] = randint(1,6)
for k,v in dados.items():
    print(f'O {k} tirou o {v} no dado.')
    sleep(1)
print('=*'*30)
print(f'{"RANKING DOS JOGADORES":>10}')
ranking = sorted(dados.items(), key=itemgetter(1),reverse=True)
for i,n in enumerate(ranking):#usar o enumerate pois é uma lista com tuplas dentro, para ver usar o print
     print(f'  {i+1}º lugar: {n[0]} com {n[1]}')
     sleep(1)


