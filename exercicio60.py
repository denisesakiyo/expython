fator = int(input("Digite um número para calcular o fatorial:"))
contador = fator
fatorial = 1
print("Calculando {}!= ".format(fator), end='')
while contador>0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial*=contador
    contador-=1
print('{}'.format(fatorial))

