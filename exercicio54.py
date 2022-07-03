import datetime
date_atual = datetime.datetime.now().year
maior = 0
menor = 0
for n in range (1,8):
   ano = int(input('Em que ano a {}ª pessoa nasceu:'.format(n)))
   idade = date_atual - ano
   if idade >18:
     maior+=1
   else:
    menor+=1
print('A quantidade de pessoas com maioridade é de {}.'.format(maior))
print('A quantidade de pessoas com menoridade é de {}.'.format(menor))