peso = float(input('Qual é o seu peso? (KG) '))
altura = float(input('Qual é a sua altura? (M) '))
indice_corporal = peso / (altura**2)
print('O IMC dessa pessoa é de {:.1f}.'.format(indice_corporal))
if indice_corporal < 18.5:
    print('Você está ABAIXO do peso! ')
elif 18.5 <= indice_corporal < 25:
    print('Você está no PESO IDEAL! ')
elif 25 <= indice_corporal < 30:
    print('Você está em SOBREPESO! ')
elif 30<= indice_corporal < 40:
    print('Você está em OBESIDADE! ')
else:
    print('Você está em OBESIDADE MÓRBIDA! ')