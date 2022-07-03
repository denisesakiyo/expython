lista = []

while True:
    nome = (str(input('Nome:')))
    n1 = float(input('Nota1: '))
    n2 = float(input('Nota2: '))
    media = (n1 + n2) / 2
    lista.append([nome,[n1,n2],media])
    continua = str(input('Quer continuar ?')).strip().upper()[0]
    if continua == 'N':
        break
print('-=' * 30)
print(f'{"nº":<4} {"Nome":<10} {"Média":>8} ')
for n, i  in enumerate(lista):
    print(f'{n:<4}{i[0]:<10}{i[2]:>8.1f}')
while True:
    print('-'*35)
    escolha = int(input('Quer mostrar as notas de qual aluno? (999 interrompe)'))
    if escolha == 999:
        print('FINALIZANDO...')
        break
    if escolha <= len(lista)-1:
        print(f'Notas de {lista[escolha][0]} são {lista[escolha][1]}')