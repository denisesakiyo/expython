sexo = str(input('Digite o seu sexo [M/F]:').upper().strip())
while sexo != 'M' and sexo != 'F':
    sexo = str(input('TENTE NOVAMENTE! Digite o seu sexo [M/F]:').upper().strip())
print('Sexo {} registrado com sucesso!'.format(sexo))

