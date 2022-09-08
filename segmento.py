a, b, c = input('Digite os tres lados do triangulo: ').split()
a = float(a)
b = float(b)
c = float(c)

if a < b + c and b < a + c and c < b + a:
    print(f'Pode criar um triângulo')
else:
    print(f'Não pode criar um triângulo')

    

