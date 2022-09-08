class Carro:
    def __init__(self):
        self.quantidade_combustivel = 0

    def __repr__(self):
        return f'Litros no tanque {self.obter_combustivel()}'
    
    def adicionar_combustivel(self, add_combu):
        self.quantidade_combustivel = add_combu
    
    def obter_combustivel(self):
      return  self.quantidade_combustivel

    def andar(self, distancia):
        while distancia > 0:
            self.quantidade_combustivel -= 0.20
            distancia -= 1

add_combu = float(input('Quanto de combustivél você quer adicionar: '))
distancia = float(input('Distancia que irá percorrer: '))
car = Carro()
car.adicionar_combustivel(add_combu)
car.andar(distancia)
print(car)