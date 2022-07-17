def linha ():
    print('-'*30)


def área(lar,comp):
    a = lar * comp
    print(f'A área  {lar} x {comp} é de {a:.2f} m²')


linha()
print('CONTROLE DE ÁREA')
linha()
l = float(input('largura (m) :'))
c = float(input('comprimento (m):'))
área(l,c)