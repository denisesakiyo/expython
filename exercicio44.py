print( (7*'-') +'LOJAS AMERICANAS' + (7*'-'))
compra = float(input ('Preço da compras: R$ '))
print ('''FORMAS DE PAGAMENTO 
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
pagamento = float(input('Qual é a opção? '))
if pagamento == 1:
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(compra,(compra *0.90)))
elif pagamento == 2:
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(compra,(compra *0.95)))
elif pagamento == 3:
    parcela = int(input('Quantas parcela? '))
    if parcela <= 2:
        print('Sua compra será parcelada em  {}X de R$ {:.2f} SEM JUROS.'.format(parcela,(compra/parcela)))
    else:
        print('Não é possivel o parcelamento SEM JUROS ')
elif pagamento == 4:
    parcela = int(input('Quantas parcela? '))
    if parcela >= 3:
        juros = compra * 1.2
        print('''Sua compra será parcelada em {}X de R$ {:.2f} COM JUROS.
Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'''.format(parcela,(juros/parcela),compra,juros))
else:
        print('OPÇÃO INVÁLIDA ')

