cnoivo = set()
cnoiva = set()
conv = input().split(';')
if len(conv) < 2:
    print('-'*20)
    print(f'LISTA FINAL')
    print('-'*20)
    print()
    print()
    print('-'*20)
    print(f'APENAS NOIVA')
    print('-'*20)
    print()
    print()
    print('-'*20)
    print(f'APENAS NOIVO')
    print('-'*20)
    print()
    print()
    print('-'*20)
    print(f'POR AMBOS')
    print('-'*20)
    print()
    print()
    print('-'*20)
    print(f'POR APENAS UM DELES')
    print('-'*20)
    print()
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
print()
lista = list(final)
lista.sort()
for items in lista:
    print(items)
print()
print('-'*20)
print(f'APENAS NOIVA')
print('-'*20)
print()
anoiva = cnoiva.difference(cnoivo)
listanoiva = list(anoiva)
listanoiva.sort()
for items in listanoiva:
    print(items)
print()
print('-'*20)
print(f'APENAS NOIVO')
print('-'*20)
print()
anoivo = cnoivo.difference(cnoiva)
listanoivo = list(anoivo)
listanoivo.sort()
for items in listanoivo:
    print(items)
print()
print('-'*20)
print(f'POR AMBOS')
print('-'*20)
print()
ambos = cnoivo.intersection(cnoiva)
listaambos = list(ambos)
listaambos.sort()
for items in listaambos:
    print(items)
print()
print('-'*20)
print(f'POR APENAS UM DELES')
print('-'*20)
print()
umdeles = cnoivo.symmetric_difference(cnoiva)
listaumdeles = list(umdeles)
listaumdeles.sort()
for items in listaumdeles:
    print(items)









