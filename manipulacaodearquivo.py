def escreve():
    arq = open('compras.txt', 'a')
    item = input('Nome do item? ')
    while item != '':
        qtd = int(input('Quantidade? '))
        arq.write(f'item: {item:14} | quantidade: {qtd}\n')
        item = input('Nome do item? ')
    arq.close()

def le1():
    arq = open('compras.txt', 'r')
    for linha in arq:
        print(linha, end='')
    arq.close()

def le2():
    arq = open('compras.txt', 'r')
    print(arq.tell(), arq.readline(), end='')
    print(arq.tell(), arq.readline(), end='')
    print(arq.tell(), arq.readline(), end='')
    print(arq.tell(), arq.readline(), end='')
    print(arq.tell(), arq.readline(), end='')
    print(arq.tell(), arq.readline(), end='')
    arq.close()

def le3():
    arq = open('compras.txt', 'r')
    texto = arq.readlines()
    for linha in texto:
        print(linha, end='')
    arq.close()

def le4():
    arq = open('compras.txt', 'r')
    texto = arq.read()
    print(texto)
    arq.close()

def le5():
    with open('compras.txt', 'r') as arq:
        for linha in arq:
            print(linha, end='')
    if arq.closed:
        print('Arquivo fechado!')
    else:
        print('Arquivo aberto!')

def le6():
    with open('compras.txt', 'r') as arq:
        print('Marcador de arquivo:', arq.tell())
        arq.seek(38)
        print('Marcador de arquivo:', arq.tell())
        print(arq.readline())
        print('Marcador de arquivo:', arq.tell())

def copia1(A, B):
    arq_A = open(A, 'r')
    arq_B = open(B, 'w')
    texto = arq_A.readlines()
    arq_B.writelines(texto)
    arq_A.close()
    arq_B.close()

def copia2(A, B):
    with open(A, 'r') as arq_A, \
         open(B, 'w') as arq_B:
        arq_B.writelines(arq_A.readlines())

copia2('compras.txt', 'copia_compras.txt')