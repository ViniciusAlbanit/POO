cnoivo = set()
cnoiva = set()
cnoivo.add('noivo')
cnoiva.add('noiva')
conv, dono = input().split(';')
if len(conv) < 1:
    print(cnoiva)
else:
    while len(conv) > 1:
        if dono == 'noivo':
            cnoivo.add(conv)
            conv, dono = input().split(';')
        else: 
            cnoiva.add(conv)
            conv, dono = input().split(';')


print(cnoivo)
print(cnoiva)





