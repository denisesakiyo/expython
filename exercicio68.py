from random import randint
v = 0
while True:
    n = int(input("Digite um valor :"))
    pc = randint(1, 10)
    total = n + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'você digitou {n} e o computador pensou em {pc}. O Total de {total}')
    print('Deu Par' if total % 2 == 0 else 'Deu impar' )
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            v+=1
        else:
            print("Você Perdeu!")
            break
    elif tipo == 'I':
        if total % 2 == 1:
            v+=1
            print('Você Venceu!')
    else:
        print('Você Perdeu!')
        break
    print('Vamos jogar novamente...')
print (f'GAME OVER!!.Você venceu {v} vezes')
