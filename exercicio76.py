compras = ('Lápis',1.75,"Caderno",10.00, 'Borracha',1.00,'Régua',2.00,
           'Compasso',5.35, 'Mochila',120.30, 'Canetas',22.65)
for n in range(0,len(compras)):
    if n % 2 == 0:
        print(f'{compras[n]:.<30}',end='')
    else:
        print(f'R$ {compras[n]:.2f}')