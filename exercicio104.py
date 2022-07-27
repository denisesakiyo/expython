def leiaInt(text):
   certo = False
   valor = 0
   while True:
       m = str(input(text))
       if m.isnumeric():
           valor = int(m)
           certo = True
       else:
           print('\033[0;31mERRO! Digite um número válido.\033[m')
       if certo:
           break
   return valor


#programa principal
n= leiaInt('Digite um número:')
print(f'Você acabou de digitar o número {n}')


