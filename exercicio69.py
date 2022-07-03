contar =  h = m = 0
while True:
    idade = int(input('Digite sua idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Seu Sexo [M/F]:')).strip().upper()[0]
    continua = ' '
    while continua not in 'SN':
        print ('=='*10)
        continua = str(input('Quer continuar [S/N]:')).strip().upper()[0]
        print('==' * 10)
    if continua == 'N':
        break
    if idade >= 18:
        contar += 1
    if sexo == 'M':
        h += 1
    else:
        if idade < 20:
             m += 1
print(f'Pessoas maiores de 18 anos: {contar}\nHomens cadastrados: {h}\nMulheres com menos de 20 anos: {m} ')

