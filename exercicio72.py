contagem = ('zero','um','dois','três','quatro','cinco',
            'seis','sete','oito','nove','dez',
            'onze','doze','treze','quatorze','quinze',
            'dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    num_digitado = int(input('Digite um número entre 0 e 20:'))
    if 0<= num_digitado <= 20:
        break
    print('Tente Novamente...',end=' ')
print(f'você digitou o número {contagem[num_digitado]}')

