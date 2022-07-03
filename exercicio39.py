import datetime
nascimento = int(input('Ano do nascimento:'))
date_atual= datetime.datetime.now().year
idade = date_atual - nascimento
alistamento = nascimento + 18

if idade < 18:
    falta = alistamento - date_atual
    print('''Quem nasceu em {} tem {} anos em {}.
Você deverà se alistar em {} anos .
Seu alistamento serà em {}'''.format(nascimento,idade,date_atual,falta,alistamento))
elif idade > 18:
    falta = date_atual - alistamento
    print('''Quem nasceu em {} tem {} anos em {}.
Voce deveria ter se alistado em  {} anos.
seu alistamento foi em  {}'''.format(nascimento,idade ,date_atual,falta,alistamento))
else:
    print(''''Quem nasceu em {} tem {} anos em {}.
Você tem que se alistar IMEDIATAMENTE.'''.format(nascimento,idade,date_atual))
