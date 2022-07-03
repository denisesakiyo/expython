matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = somas = maior = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {[linha,coluna]}: '))
        if matriz [linha][coluna] % 2 == 0:
            soma += matriz [linha][coluna]
        if matriz[linha][2]:
            somas +=matriz[linha][2]
        if matriz [1][coluna] > maior:
            maior = matriz[1][coluna]

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end=' ')
    print()
print (f'A soma dos valores pares é de {soma}')
print(f'A soma de valores da terceira coluna é de {somas} ')
print(f'O maior valor da segunda linha é de {maior}')

