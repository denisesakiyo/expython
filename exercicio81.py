lista = []
while True:
    lista.append( int(input('Digite um valor: ')))
    continua = str(input('Você que continuar ? [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        break
lista.sort(reverse=True)
print(f"Você digitou {len(lista)} elementos.")
print(f"A lista em forma decrescente é {lista}")
if 5 in lista:
    print('o número 5 está na lista')
else:
    print('O número 5 não está na lista')



