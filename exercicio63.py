termo = int(input("Quantos termos quer digitar: "))
t1=0
t2=1
contar = 3
print('{} {}'.format(t1,t2),end=' ')
while contar<=termo:
    t3=t1+t2
    t1=t2
    t2=t3
    contar+=1
    print('{}'.format(t3),end=' ')