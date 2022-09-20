cnoivo = set()
cnoiva = set()
cnoivo.add('noivo')
cnoiva.add('noiva')
conv = input().split(';')
if len(conv) < 2:
    print(cnoiva)
else:
    while len(conv) > 1:
        if conv[1] == 'noivo':
            cnoivo.add(conv[0])
            conv = input().split(';')
        else: 
            cnoiva.add(conv[0])
            conv = input().split(';')

final = cnoivo.union(cnoiva)

print('-'*20)
print(f'LISTA FINAL')
print('-'*20)
print(sorted(final))
print()
print('-'*20)
print(f'APENAS NOIVA')
print('-'*20)
print(sorted(cnoiva))
print()
print('-'*20)
print(f'APENAS NOIVO')
print('-'*20)
print(sorted(cnoivo))
print()
print('-'*20)
print(f'POR AMBOS')
print('-'*20)
ambos = cnoivo.intersection(cnoiva)
print(sorted(ambos))
print()
print('-'*20)
print(f'POR APENAS UM DELES')
print()




