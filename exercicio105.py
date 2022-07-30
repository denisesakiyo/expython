def notas(*dic, sit = False):
    x={}
    x['Tamanho'] = len(dic)
    x['Maior Nota'] = max(dic)
    x['Menor Nota'] = min(dic)
    x['Média'] = sum(dic)/len(dic)

    if sit:
        if x['Média'] >= 7:
            x['Situação'] = 'BOA'
        elif x ['Média']>=5:
            x['Situação'] = 'Razoável'
        else:
            x['Situação'] = 'Ruim'
    return x





#programa principal
resp = notas(3.5,2.0,6.0,4,sit = True)
print(resp)