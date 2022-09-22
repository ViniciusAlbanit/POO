class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
class VeiculoNaoRegistrado(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
class VeiculoRegistrado(Veiculo):
    def __init__(self, marca, modelo, placa):
        super().__init__(marca, modelo)
        self.placa = placa
class Bicicleta(VeiculoNaoRegistrado):
    def __init__(self, marca, modelo, material, marchas):
        super().__init__(marca, modelo)
        self.material = material
        self.marchas = marchas
    def exibir(self):
        print('---------------------')
        print('Marca:', self.marca)
        print('Modelo:', self.modelo)
        print('Material:', self.material) 
        print('Marchas:', self.marchas) 

class Moto(VeiculoRegistrado):
    def __init__(self, marca, modelo, placa, guidão):
        super().__init__(marca, modelo, placa)
        self.guidão = guidão
    def exibir(self):
        print('---------------------')
        print('Marca:', self.marca)
        print('Modelo:', self.modelo)
        print('Placa:', self.placa)
        print('Guidão: ', self.guidão)

class Carro(VeiculoRegistrado):
    def __init__(self, marca, modelo, placa, portas, lugares):
        super().__init__(marca, modelo, placa)
        self.portas = portas
        self.lugares = lugares
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, placa, portas, lugares, bateria):
        super().__init__(marca, modelo, placa, portas, lugares)
        self.bateria = bateria
    def exibir(self):
        print('---------------------')
        print('Marca:', self.marca)
        print('Modelo:', self.modelo)
        print('Placa:', self.placa)
        print('Portas:', self.portas)
        print('Bateria: ', self.bateria)
   
class CarroCombustão(Carro):
    def __init__(self, marca, modelo, placa, portas, lugares, tanque):
        super().__init__(marca, modelo, placa, portas, lugares)
        self.tanque = tanque
    def exibir(self):
        print('---------------------')
        print('Marca:', self.marca)
        print('Modelo:', self.modelo)
        print('Placa:', self.placa)
        print('Portas:', self.portas)
        print('Tanque: ', self.tanque)

cc = CarroEletrico('Tesla', 'Tesla1', 'abcd1234', 2, 4, 400)
ce = CarroCombustão('Ferrari', 'F850', 'vrcd1234', 2, 4, 100)
m1 = Moto('Harley Davison', 'Fat Boy', 'fdubv', 1)
b1 = Bicicleta('Caloy', 'Aventor', 'Adamantium', 20)

cc.exibir()
ce.exibir()
m1.exibir()
b1.exibir()
