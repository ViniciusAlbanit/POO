class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimetro(self):
       return self.lado_a + self.lado_b + self.lado_c
    
    def __repr__(self):
        return f'Perimetro: {self.calcular_perimetro()} \n'+ \
                f'Lado A: {self.lado_a} |'+ \
                f'Lado B: {self.lado_b} |'+ \
                f'Lado C: {self.lado_c} |'


lado_a = float(input('Lado A: '))
lado_b = float(input('Lado B: '))
lado_c = float(input('Lado C: '))
Tri = Triangulo(lado_a, lado_b, lado_c)
print(Tri)
