from posixpath import split
cnoivo = set('noivo')
cnoiva = set('noiva')
nome, noivos = input(), split(';')
while nome != 'ACABOU':
    if noivos == 'noivo':
        cnoivo.add(nome)
    elif nome == 'ACABOU':
        break
    else:
        cnoiva.add(nome)


    
    

print(cnoivo)
print(cnoiva)






