from random import randint
soma = 1
print('''Sou seu computador... \nAcabei de pensar em um número entre 0 e 10.
Será que você consegue advinhar qual foi?''')
num = int(input('Qual é o seu palpite? '))
pc_pensa = randint(0,10)
while num != pc_pensa:
    if num > pc_pensa:
        print('O número é menor, TENTE NOVAMENTE!')
    else:
        print('O número é maior, TENTE NOVAMENTE!')
    num = int(input("Qual o seu novo palpite? "))
    soma+=1
print("VOCÊ ACERTOU!! O número é {} e você tentou {} vezes".format(pc_pensa,soma))
