palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','CURSO',
            'GRATIS','TRABALHAR','MERCADO',
            'PYTHON','PROGRAMADOR')
for n in palavras:
    print (f'\nNa palavra {n} temos ',end='')
    for letra in n:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')

