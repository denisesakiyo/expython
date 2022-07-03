maior = menor = num = contar = soma = 0
continua = ''
while continua in 'Ss':
    num = int(input("Digite um número:"))
    contar+=1
    soma+=num
    media = soma / contar
    if contar==1:
        maior = menor = num
    else:
        if num>maior:
            maior = num
        if num<menor:
            menor = num
    continua = str(input('Deseja continuar [S/N]')).upper().strip()[0]
print('Você digitou {} números e a média deles é de {}'.format(contar,media))
print('O maior valor foi de {} e o menor valor {}'.format(maior,menor))
