class Pessoa:
    def __init__(self, identificador, nome):
        self.identificador = identificador
        self.nome = nome

class PessoaJuridica(Pessoa):
    def __init__(self, identificador, nome, cnpj):
        super().__init__(identificador, nome)
        self.cnpj = cnpj
class PessoaFisica(Pessoa):
    def __init__(self, identificador, nome, rg, cpf):
        super().__init__(identificador, nome)
        self.rg = rg
        self.cpf = cpf