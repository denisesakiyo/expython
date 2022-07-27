def ficha(nome ="desconhecido", gols=0):
    print(f'O jogador {nome} fez {gols} gols.')


nome = str(input('Digite o Jogador:'))
gols = str(input('Quantos gols foram feitos:'))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols = gols)
else:
    ficha(nome,gols)