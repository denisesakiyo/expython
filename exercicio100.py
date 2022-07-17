from random import randint
lista = []

def sortear():
    cont =0
    while True:
        num = randint(1,10)
        if num not in lista:
            lista.append(num)
            cont+=1
            if cont==5:
                break

    print(f'Os números sorteados foram {lista}.')


def somapar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n

    print(f'Os números sorteados foram {lista} e a soma dos pares é de {soma}.')


sortear()
somapar(lista)