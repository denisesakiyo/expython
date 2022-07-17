def maior(*num):
    print()
    print("Analizando os valores...")
    cont = maior = 0
    for n in num:
        print(f'{n}',end=' ')
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont+=1
    print(f"Foram informados {cont} valores.")
    print(f"O maior valor informado é {maior}")


#programa principal
maior (2,7,3,4,8,9)
maior (1,2,3)
maior (5,8)
maior()