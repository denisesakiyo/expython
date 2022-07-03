num = []
for c in range(0,5):
   num.append(int(input(f"Digite um valor {c}º:")))

print(f"Os números que foram digitados são os seguintes : {num}")
print(f"O maior valor é {max(num)} que está na posição",end='')
for pos,valor in enumerate(num):
   if max(num)==valor:
      print(f" {pos}º",end='....')

print(f'\nO menor valor é {min(num)} que está na posição', end='')
for pos, valor in enumerate(num):
   if min(num)==valor:
      print(f' {pos}º',end='...')
