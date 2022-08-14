def aumenta(preço=0,taxa=10,formato=False):
    n = preço *((100+taxa)/100)
    #print(f'O valor do aumento é de {taxa}% e o novo valor será de {moeda (n,)}.')
    return n if not formato else moeda(n,)


def diminui(preço=0,taxa=5,formato=False):
    d = preço *((100-taxa)/100)
    #print(f'O valor do diminuiu em  {taxa}% e o novo valor é de {moeda (d,)}.')
    return d if not formato else moeda(d,)


def dobro(preço=0,formato=False):
    do=preço*2
    #print(f'O valor é de {moeda (preço)} e seu dobro é {moeda (do,)}')
    return do if not formato else moeda(do,)


def metade(preço=0,formato=False):
    m = preço /2
    #print(f'O valor é de {moeda (preço)} e sua metade é {moeda (m,)}')
    return m if not formato else moeda(m)

def moeda(preço=0,moeda='R$'):
    return (f'{moeda}{preço:.2f}'.replace('.',','))

def resumo(valor,aumento,redução):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado:\t{moeda(valor)}')
    print(f'Dobro do preço:\t\t{dobro(valor,True)}')
    print(f'Metade do preço:\t{metade(valor,True)}')
    print(f'{aumento} % de aumento:\t{aumenta(valor,aumento,True)}')
    print(f'{redução} % de redução:\t{diminui(valor,redução,True)}')
    print('-'*30)
#\t é uma tabulação