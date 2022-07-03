jogo = {}
gols = []
jogo['nome']=str(input('Nome do Jogador:'))
partidas =int(input(f'Quantas partidas o {jogo["nome"]} jogou?'))
for c in range(0,partidas):
    gols.append(int(input(f'     Quantos gols na partida {c}?')))
    jogo['gols'] = gols[:]
    jogo['total']= sum(gols)
print('=*='*20)
print(jogo)
print('=*='*20)

for k,v in jogo.items():
    print(f'O campo {k} tem valor {v}')
print('=*='*20)
print(f'O jogador {jogo["nome"]} jogou {partidas} partidas.')

for i, n in enumerate(gols):
    print(f'    =>Na partida {i}, fez {n} gols.')
print(f'Foi um total de {jogo["total"]} gols.')
