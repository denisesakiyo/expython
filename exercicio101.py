from _datetime import datetime

print('-' * 30)
ano = int(input('Ano de nascimento:'))


def voto(ano):
    idade =  datetime.now().year - ano
    if 18 < idade < 70 :
        print (f'A idade é de {idade}. O voto é  OBRIGATÓRIO!')
    elif idade >= 70 or 16<idade<18:
        print(f'A idade é de {idade}. O voto é OPCIONAL!')
    else:
        print(f'A idade é de {idade}. O voto é NEGADO!')


voto(ano)