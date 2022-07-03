tabuada = 0
while True:
    tabuada = int(input('Digite qual tabuada quer ver:'))
    if tabuada < 0:
        break
    for i in range(1,11):
        print(f'{tabuada} x {i} = {tabuada*i}')
print ('PROGRAMA DE TABUADA ENCERRADO, VOLTE SEMPRE!')

