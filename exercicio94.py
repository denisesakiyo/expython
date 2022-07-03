dados = {}
lista = []
while True:
    dados['nome'] = str(input('Nome:'))
    dados['sexo'] = str(input('Sexo:')).strip().upper()

    while dados['sexo'] !='F' and dados['sexo']!='M':
        print('ERRO!Digite apenas M ou F')
        dados['sexo'] = str(input('Sexo:')).strip().upper()
    else:
        dados['idade'] = int(input('Idade:'))
        continua = str(input('Quer continuar [S/N]:')).upper().strip()
    while continua != 'S' and continua!= 'N':
        print('ERRO!Responda apenas S ou N')
        continua = str(input('Quer continuar [S/N]:')).upper().strip()
    if continua == 'N':
        break

print('=*='*25)
print(f'A) Ao todo temos {} pessoas cadastradas')

