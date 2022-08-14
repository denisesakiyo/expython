def aumenta(preço,taxa):
    n = preço *((100+taxa)/100)
    print(f'O valor do aumento é de {taxa}% e o novo valor será de {moeda (n,)}.')
    return n


def diminui(preço,taxa):
    d = preço *((100-taxa)/100)
    print(f'O valor do diminuiu em  {taxa}% e o novo valor é de {moeda (d,)}.')
    return d


def dobro(preço):
    do=preço*2
    print(f'O valor é de {moeda (preço)} e seu dobro é {moeda (do,)}')
    return do


def metade(preço):
    m = preço /2
    print(f'O valor é de {moeda (preço)} e sua metade é {moeda (m,)}')
    return m

def moeda(preço=0,moeda='R$'):
    return (f'{moeda}{preço:.2f}'.replace('.',','))