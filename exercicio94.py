dados = {}
lista = []
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome:'))
    while True:
        dados['sexo'] = str(input('Sexo:')).strip().upper()
        if dados['sexo'] in 'FM':
            break
        print('ERRO!Digite apenas M ou F')
    dados['idade'] = int(input('Idade:'))
    soma+=dados['idade']
    lista.append(dados.copy())
    while True:
        continua = str(input('Quer continuar [S/N]:')).upper().strip()
        if continua in 'SN':
            break
            print('ERRO!Responda apenas S ou N')
    if continua == 'N':
        break

print('=*='*25)
print(lista)
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas')
media = soma / len(lista)
print(f'B) A média de idade é de {media:5.2f}')
print(F'C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]}',end='')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for p in lista:
    if p['idade'] >= media:
        print('  ',end=' ')
        for k,v in p.items():
            print(f'{k} = {v}',end=' ')
print('<<ENCERRADO<<')

