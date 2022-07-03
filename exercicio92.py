from datetime import datetime
trabalho = {}


trabalho['Nome'] = str(input('Nome:'))
nasc = int(input('Ano de nascimento:'))
trabalho['idade'] = datetime.now().year - nasc
trabalho['carteira'] = int(input('Carteira de Trabalho (0 não tem):'))
if trabalho['carteira'] != 0:
    trabalho['Contrato'] = int(input('Ano de Contratação: '))
    trabalho['Salário'] = float(input('Salário: R$ '))
    trabalho['Aposentadoria'] = trabalho['idade']+((trabalho['Contrato'] + 35) - datetime.now().year)
for k,v in trabalho.items():
    print(f'O {k} tem valor {v}.')
