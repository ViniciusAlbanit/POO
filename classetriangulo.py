class triangulo:
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


a = float(input('Lado A: '))
b = float(input('Lado B: '))
c = float(input('Lado C: '))
Tri = triangulo(a, b, c)
print(Tri)
