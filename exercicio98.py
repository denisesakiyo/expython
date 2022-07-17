from time import sleep


def contador(i,f,p):
    if p< 0:
        p*=-1
    if p == 0:
        p=1
    print('-'*30)
    print(f'Contagem de {i} a {f} de {p}')
    if i<f:
        cont = i
        while cont<=f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.2)
            cont+=p
    else:
        if i > f:
            cont = i
            while cont >= f:
                print(f'{cont}', end=' ',flush=True)
                sleep(0.2)
                cont -= p
    print('FIM!')
    print('-' * 30)


contador (1,10,1)
contador(10,3,2)
print('Agora é sua vez de personalizar a contagem.')
ini = int(input('Início:'))
fim = int(input('Fim: '))
pas= int(input('Passo: '))
contador(ini,fim,pas)

