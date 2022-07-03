menor = 0
maior = 0
for p in range(1,6):
    peso = float(input('Peso da {}ª pessoa:'.format(p)))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
           maior = peso
        if peso < menor:
           menor = peso
print('O Maior peso é de {}KG'.format(maior))
print('O Menor peso é de {}kG'.format(menor))
