class Fila:
    def __init__(self, tamanho):
        self.__itens = tamanho * [None]
        self.__inicio = 0
        self.__fim = 0
    
    def vazia(self):
        return self.__fim == self.__inicio

    def cheia(self):
        return self.__fim == len(self.__itens)    

    def enfileira(self, valor):
        if self.cheia():
            print('Operação invalida fila cheia')
            exit()
        self.__itens[self.__fim] = valor
        self.__fim += 1
    
    def desenfileira(self, valor):
        if self.__vazia():
            print('Operação invalida fila cheia')
            exit()
        item = self.__itens[self.__inicio]
        i = 0
        while i <= fim-2:
            self.__itens[i] = self.__itens[i + 1]
            i += 1
        return item

    def destroi(self):
        self.__fim = self.__inicio

