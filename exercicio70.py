total = cont = menor = contar = 0
barato = ' '
while True:
    prod = str(input ('Nome do Produto:'))
    valor = float(input('Preço :  R$ '))
    continuar = ' '
    total += valor
    cont +=1
    if valor > 1000:
        contar += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = prod
    while continuar not in 'SN':
        continuar = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'O valor gasto foi de: R$ {total:.2f}\nTemos {contar} que custam mais de R$ 1000.00\nO produto mais barato é {barato} que custa R$ {menor:.2f}')







