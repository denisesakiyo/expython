valor = int(input ("Digite um valor inteiro:"))
print ('''Escolha uma das bases para conversão: 
1- converter para a base binária
2- converter para a base octal
3- converter para a base hexadecimal''')
opcao = int(input('Sua opção:'))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(valor,bin(valor)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(valor,oct(valor)[2:]))
elif opcao == 3:
    print ('{} convertido para HEXADECIMAL é igual a {}'.format(valor,hex(valor)[2:]))
else:
    print('Opção Inválida.Tente Novamente')


