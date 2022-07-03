frase = str (input('Digite uma frase:'))
invertida = frase[::-1]
mudar1 = frase.upper().replace(' ','')
mudar2 = invertida.upper().replace(' ','')
if mudar1 == mudar2 :
    print('\nA frase {} invertida {}. \nÉ um PALÍNDROMO!'.format(mudar1,mudar2))
else:
    print('\nA frase {} invertida {}.\nNÃO é PALÍNDROMO'.format(mudar1,mudar2))

