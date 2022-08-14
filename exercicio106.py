



print('SISTEMA DE AJUDA PYHELP...')
print()
while True:
    n = str(input('Digite uma função ou biblioteca:')).upper().strip()
    if n == 'FIM':
        break
    print(help(n))