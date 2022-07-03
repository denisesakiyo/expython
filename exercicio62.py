print('GERADOR DE P.A')
termo = primeiro = int(input('Digite o primeiro termo da sua PA: '))
razao = int(input('Digite a razão de sua PA: '))
contar = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contar < total:
        print("{}".format(termo),end='-')
        termo+=razao
        contar+=1
    mais = int(input('\nQuantos termos você quer mostrar a mais ?'))
print('Progressão finalizada com {} termos mostrados.'.format(total),end=' ')

