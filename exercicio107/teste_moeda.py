def aumenta(preço,taxa):
    n = preço *((100+taxa)/100)
    print(f'O valor do aumento é de {taxa}% e o novo valor será de R$ {n:.2f}.')
    return n


def diminui(preço,taxa):
    d = preço *((100-taxa)/100)
    print(f'O valor do diminuiu em  {taxa}% e o novo valor é de R$ {n:.2f}.')
    return d


def dobro(preço):
    do=preço*2
    print(f'O valor é de R$ {preço} e seu dobro é R$ {do:.2f}')
    return do


def metade(preço):
    m = preço /2
    print(f'O valor é de R$ {preço} e sua metade é R$ {m:.2f}')
    return m