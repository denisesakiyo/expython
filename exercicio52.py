print ('DESCOBRINDO SE O NÚMERO É PRIMO OU NÃO ')
num = int (input('Digite um número:'))
total = 0
for n in range (1,num+1):
    if num % n == 0:
        print('\033[31m', end=' ')
        total += 1
    else:
        print('\033[33m', end=' ')
    print('{}'.format(n), end=' ')

print('\n\033[mO número {} foi dividido {} vezes.'.format(num,total),end=' ')
if total < 3:
    print ('\nE por isso o número {} É PRIMO.'.format(num))
else:
    print('\nE por isso o número {} NÃO É PRIMO'.format(num))


