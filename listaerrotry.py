def funcao_ex02():
    print('Início da função')
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try:
        for i in range(15):
            print(lista[i])
    except IndexError:
        print('Índice fora do intervalo')
    print('Fim da função')

print('Início do programa')
funcao_ex02()
print('Fim do programa')
