n = (int(input('Digite um número:')),int(input('Digite outro número:')),
         int(input('Digite mais um número:')), int(input('Digite o último número:')))

print(f'Você digitou o seguintes números {n}')
print(f'O número 9 apareceu {n.count(9)} vezes')
if 3 in n :
    print(f'O número 3 está na posição {n.index(3)+1}º')
else:
    print('O valor 3 não apareceu nenhuma vez.')
print('Os números pares são:',end='' )
for num in n :
    if num % 2 == 0:
        print(f'{num}',end=' ')