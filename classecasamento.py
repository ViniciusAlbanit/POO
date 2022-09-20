cnoivo = set()
cnoiva = set()
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
for items in final:
    print(items)
    sorted(final)
print()
print('-'*20)
print(f'APENAS NOIVA')
print('-'*20)
anoiva = cnoiva.difference(cnoivo)
for items in anoiva:
    sorted(anoiva)
    print(items)
print()
print('-'*20)
print(f'APENAS NOIVO')
print('-'*20)
anoivo = cnoivo.difference(cnoiva)
for items in anoivo:
    sorted(anoivo)
    print(items)
print()
print('-'*20)
print(f'POR AMBOS')
print('-'*20)
ambos = cnoivo.intersection(cnoiva)
for items in ambos:
    sorted(ambos)
    print(items)
print()
print('-'*20)
print(f'POR APENAS UM DELES')
print('-'*20)
umdeles = cnoivo.symmetric_difference(cnoiva)
for items in umdeles:
    sorted(umdeles)
    print(items)








