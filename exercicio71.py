valor = int(input('Qual o valor a ser sacado: R$ '))
cedula1 = cedula2 = cedula3 = cedula4 = contar = totalced= 0
while True:
    if valor >= 50:
        cedula1 = valor // 50
        valor = valor % 50
        print(f'Total de {cedula1} cédulas de R$ 50,00')
    elif 20<=valor<50:
        cedula2 = valor //20
        valor = valor % 20
        print(f'Total de {cedula2} cédulas de R$ 20,00')
    elif 10<= valor < 20:
        cedula3 = valor // 10
        valor = valor % 10
        print(f'Total de {cedula3} cédulas de R$ 10,00')
    else:
        cedula4 = valor
        if cedula4 !=0:
           print(f'Total de {cedula4} cédulas de R$ 1,00')
        break




