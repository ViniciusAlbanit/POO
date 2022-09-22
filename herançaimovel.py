class Imovel:
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco

class ImovelNovo(Imovel):
    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco, preco)
        self.adicional = adicional
def calcular_preco(self):
        return self.preco + self.adicional

class ImovelVelho(Imovel):
    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)
        self.desconto = desconto

    def calcular_preco(self):
        return self.preco - self.desconto 