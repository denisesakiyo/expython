lista = []
lista_par =[]
lista_impar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continua = str(input('Deseja continuar ? [S/N]: '))
    if continua in 'nN':
        break
for c in lista:
    if c % 2 == 0 :
        lista_par.append(c)
    else:
        lista_impar.append(c)
print("=*="*30)
print(f'A lista completa {lista}')
print(f'A lista só com número pares {lista_par}')
print(f'A lista só com números ímpares {lista_impar}')
