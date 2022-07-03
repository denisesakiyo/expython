x = float(input('Qual o valor da casa?'))
y = float(input('O salário do comprador?'))
z = float(input ('Quantos anos de financiamento?'))
a = x/(z*12)
b = y * 0.3
if  a > b:
    print ('Para pagar uma casa de R$ {:.2f} em {:.0f} anos a prestação será de R$ {:.2f} \nEmpréstimo NEGADO!'.format(x,z,a))
else:
    print('Para pagar uma casa de R$ {:.2f} em {:.0f} anos a prestação será de R$ {:.2f}\nEmpréstimo ACEITO!'.format(x,z,a))
