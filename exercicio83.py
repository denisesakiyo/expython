expressão = str(input('Digite a sua expressão:'))
cont = 0
for c in expressão:
    if c == '(' :
        cont+=1
    if c== ')':
        cont-=1
    if cont < 0:
        break
if cont == 0:
    print(f'A sua expressão é válida...')
else:
    print(f'A sua expressão é inválida...')

#expressão = str(input('Digite a sua expressão:'))
#pilha = []
#for simb in expressão:
#   if simb == '(':
#        pilha.append('(')
#    elif simb == ')':
#        if len(pilha)>0:
#            pilha.pop() POP RETIRA O ÚLTIMO ELEMENTO DA PILHA
  #        else:
#            pilha.append(')')
#if len(pilha)==0:
#    print('sua expressão é válida ')
#else:
#   print('Sua expressão é inválida')
