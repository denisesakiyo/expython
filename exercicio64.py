num=contar=soma=0
num = int(input('Digite um número [999 para parar ]:'))

while num != 999:
    contar+=1
    soma+=num
    num = int(input('Digite um número [999 para parar ]:'))
print("Você digitou {} números e a soma deles é de {}".format(contar,soma))
