def fatorial (n,show = False):
    """
    ->Calcule o Fatorial de um número
    :param n: número a ser calculado
    :param show: opcional,mostrar ou não a conta
    :return: valor fatorial de um número n
    """
    fat = 1
    for c in range(n,0,-1):
        if show:
            print(c,end='')
            if c>1:
                print('x', end='')
            else:
                print('=',end='')
        fat*=c
    return fat


n = int(input('Digite um número para o calcúlo do fatorial: '))
print(fatorial(n,show=True))