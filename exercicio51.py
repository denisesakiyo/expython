print('='* 50)
print('10 PRIMEIROS TERMOS DE UMA P.A')
print('='* 50)

pri_termo = int (input("Digite o primeiro termo:"))
razao = int(input( 'Digite a razão:'))
décimo_termo = int( pri_termo + 9 * razao)

for p in range(pri_termo,décimo_termo + 1,razao):
    print('{}'.format(p),end= '-'
                              '')
print('ACABOOOOOUUUUU!!')