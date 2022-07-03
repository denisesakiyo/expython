times = ('Corinthians','Santos','Avaí','América - MG','Bragantino',
         'Atlético - MG','São Paulo','Botafogo','Internacional',
         'Coritiba','Cuiabá','Athletico - PR','Palmeiras',
         'Flamengo','Fluminense','Goiás','Ceará','Juventude',
         'Atlético - GO','Fortaleza')
print(f'Os cinco primeiros colocados são : {times[0:5] }')
print(f'Os últimos quatro colocados são: {times[16:21]}')
print(f'OS Times em ordem álfabética: {sorted(times)}')
print(f'O time Flamengo está na {times.index("Flamengo")+1}º posição ')


