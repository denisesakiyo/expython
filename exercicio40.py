p1 = float(input ('Primeira Nota:'))
p2 = float (input('Segunda Nota:'))
media = ((p1+p2)/2)
if media < 5:
    print('Tirando {} e {} a sua mèdia è de {:.1f}.\nO aluno està REPROVADO'.format(p1,p2,media))
elif media > 7:
    print('Tirando {} e {} a sua mèdia è de {:.1f}.\nO aluno està APROVADO'.format(p1,p2,media))
else:
    print('Tirando {} e {} a sua mèdia è de {:.1f}.\nO aluno està de RECUPERAÇÃO.'.format(p1,p2,media))
