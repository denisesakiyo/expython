num = []
while True:
    numero = int(input("Digite um valor:"))
    if numero not in num:
        num.append(numero)
        print(f'Valor adicionado com sucesso...')
    else:
        print(f'Valor duplicado, não pode ser adicionado')
    resposta = str (input (f"Quer continuar? [S/N]")).strip()[0]
    if resposta in 'Nn':
        break
num.sort()
print (f"Os valores digitados foram {num}")
