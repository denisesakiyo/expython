alunos = {}

alunos['nome'] = str(input('Nome:'))
alunos['media'] = float(input('Média:'))
if alunos['media'] >=7:
   alunos['Situação'] = 'APROVADO'
elif 5 <= alunos['media'] < 7:
   alunos['Situação'] = 'RECUPERAÇÃO'
else:
    alunos['Situação'] = 'REPROVADO'

for k,v in alunos.items():
    print(f'A {k} é igual a {v}.')
