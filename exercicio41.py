from datetime import date
ano_atual= date.today().year
ano = int( input("Ano de Nascimento:") )
idade = ano_atual - ano
if idade <= 9:
    print('O atleta tem {} anos. \nCategoria: MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos. \nCategoria: INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos. \nCategoria: JÚNIOR'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos. \nCategoria: SÊNIOR'.format(idade))
else:
    print('O atleta tem {} anos. \nCategoria: MASTER'.format(idade))