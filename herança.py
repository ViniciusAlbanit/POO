class Veiculo:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
class Carro(Veiculo):
    def __init__(self, marca, modelo, placa, portas):
        super().__init__(marca, modelo, placa)
        self.portas = portas

    def exibir(self):
        print('---------------------')
        print('Marca:', self.marca)
        print('Modelo:', self.modelo)
        print('Placa:', self.placa)
        print('Portas:', self.portas)

c1 = Carro('Ferrari', 'F850', 'abcd1234', 2  )

c1.exibir()
            