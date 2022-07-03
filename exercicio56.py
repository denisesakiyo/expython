soma_idade= 0
maior_idade_homem=0
nome_velho =''
total_mulher20=0
for d in range(1,5):
    dados = print('----{}ª PESSOA----'.format(d))
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:'))
    soma_idade+=idade
    if d == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade >maior_idade_homem:
            maior_idade_homem = idade
            nome_velho = nome
    if sexo in 'Ff' and idade < 20:
                total_mulher20+=1
media = soma_idade/4
print('A média da idade do grupo é de {} anos.'.format(media))
print('O nome do homem mais velho é {}.'.format(nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(total_mulher20))