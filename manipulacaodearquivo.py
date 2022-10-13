def escreve():
    arq = open('compras.txt', 'w')
    item = input('Nome do item: ')
    while item != '':
        qtd = int(input('Quantidade: '))
        arq.write(f'item: {item} | quantidade: {qtd}')
        item = input('Nome do item: ')
def le():
    arq = open('compras.txt', 'r')
    for linha in arq:
        print(linha)

escreve()
le()