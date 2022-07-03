print('GERADOR DE P.A')
primeiro = int(input('Digite o primeiro termo da sua PA: '))
razao = int(input('Digite a razão de sua PA: '))
decimo_termo = 0
termo = primeiro

while decimo_termo < 10:
    print("{}".format(termo),end='')
    print(' --> ' if decimo_termo < 9 else ' \n',end='')
    termo+=razao
    decimo_termo+=1
print('ACABOU')