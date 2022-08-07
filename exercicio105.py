def notas(*dic, sit = False):
    n= {}
    n['total'] = len(dic)
    n['Maior'] = max(dic)
    n['Menor'] = min(dic)
    n['Média'] = sum(dic)/len(dic)
    if sit:
        if n['Média']>=7:
            n['Situação'] = 'BOA'
        elif n['Média']>=5:
            n['Situação'] = 'RAZOAVÉL'
        else:
            n['Situação'] = 'RUIM'
    return n
    
#programa principal
resp = notas(2.5,10,10,5,sit=True)
print(resp)