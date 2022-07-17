jogo = {}
gols = []
novo_jogador = []
while True:
    jogo.clear()
    gols.clear()
    jogo['nome']=str(input('Nome do Jogador:'))
    partidas =int(input(f'Quantas partidas o {jogo["nome"]} jogou?'))
    for c in range(0,partidas):
        gols.append(int(input(f'     Quantos gols na partida {c}?')))
    jogo['gols'] = gols[:]
    jogo['total']= sum(gols)
    novo_jogador.append(jogo.copy())
    while True:
        continua = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if continua in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continua == 'N':
        break
print('=*=' * 20)
print('cod',end=' ')
for i in jogo.keys():
    print(f'{i:<15}',end=' ')
print()
print('-'*40)
for k,v in enumerate(novo_jogador):
    print(f'{k:>3}',end=' ')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()

print('=*='*20)
while True :
    busca = int(input('Mostrar dados de qual jogador?(999 para parar)'))
    if busca == 999:
        break
    if busca >= len(novo_jogador):
        print(f'ERRO!Não existe o jogador com o código {busca}')
    else:
        print(f'LEVANTAMENT DO JOGADOR {novo_jogador[busca]["nome"]}')
        for i, g in enumerate(novo_jogador[busca]['gols']):
            print(f'No jogo {i} fez {g} gols')
        print('-'*40)
print('VOLTE SEMPRE!')

