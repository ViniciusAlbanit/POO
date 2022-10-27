class Pilha:
    def __init__(self, tamanho):
        self.__itens = tamanho * [None]
        self.__topo = -1

    def __repr__(self):
        s = '|'
        for item in self.__itens[:self.__topo+1]:
            s += ' ' + str(item) + ' |'
        s += f'\nTopo -> {self.__topo}' 
        return s

    def vazia(self):
        return self.__topo == -1

    def cheia(self):
        return self.__topo == len(self.__itens)-1

    def empilha(self, valor):
        if self.cheia():
            print('Operação inválida! Pilha cheia')
            exit()
        self.__topo += 1
        self.__itens[self.__topo] = valor

    def desempilha(self):
        if self.vazia():
            print('Operação inválida! Pilha vazia')
            exit()
        item = self.__itens[self.__topo]
        self.__topo -= 1
        return item

    def destroi(self):
        self.__topo = -1
