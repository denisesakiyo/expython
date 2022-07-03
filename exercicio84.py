maior = menor = 0
lista = []
principal = []
while True:
    nome = lista.append((str(input('Digite o seu nome:'))))
    peso = lista.append( (float(input('Qual o seu peso?'))))
    continua = str(input('Quer continuar?[s/n]:')).upper().strip()[0]
    if len(principal)== 0:
        maior = menor = lista[1]
    else:
        if lista[1]> maior:
            maior = lista[1]
        if lista[1]<menor:
            menor = lista[1]
    principal.append(lista[:])
    lista.clear()
    if 'N' in continua:
        break
print(f'O número de pessoas que foram cadastradas é de {len (principal)}')
print(f'O maior peso foi de {maior}kg',end=' ')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}]')
print(f'O menor peso foiu de {menor} kg',end=' ')
for n in principal:
    if n[1] == menor:
        print(f'[{n[0]}]')