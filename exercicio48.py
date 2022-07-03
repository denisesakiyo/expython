soma = 0
qtd = 0
for cont in range(1,501,2):
    if cont % 3==0:
        soma += cont
        qtd +=1
print('A soma dos {} números ímpares e múltiplos de 3 é de {}.'.format(qtd,soma))
