from time import sleep
x = 0
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
while x < 5:
    print('==*==' * 5)
    print('''Escolha uma opção:\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa''')
    print('==*==' * 5)
    x = int(input(">>>>> Qual a sua opção:"))
    if x == 1:
        print ('A soma de {} e {} é {}'.format(num1,num2,num1+num2))
    elif x == 2:
        print('a multiplicação de {} e {} é de {}'.format(num1,num2,num1*num2))
    elif x == 3:
        if num1>num2:
            print('O maior número entre {} e {} é {}'.format(num1,num2,num1))
        else:
            print('O maior número entre {} e {} é {}'.format(num1,num2,num2))
    elif x == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite um número: '))
    elif x == 5:
        print('Finalizando')
        sleep(1)
        print("=-="*7)
        print("Fim do programa!Volte sempre")
    else:
        print("Opção inválida.Tente novamente!")
