l1 = float(input('Primeiro Segmento:'))
l2 = float(input('Segundo Segmento:'))
l3 = float(input('Terceiro Segmento:'))

if l3 < l1 + l2 and l2 < l1+l3 and l1 < l2+l3:
    print('Os segmentos acima PODEM formar um triângulo ', end='')
    if l1==l2==l3:
        print ('EQUILÁTERO!')
    elif l1!=l2 and l1!=l3 and l2!=l3:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um TRIÂNGULO.')





