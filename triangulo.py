a, b, c = input('Digite os lados do triangulo: ').split()
a = int(a)
b = int(b)
c = int(c)

if a == b == c:
    print('O triângulo é equilátero')
elif a != b == c or b != a == c or c!= b == a:
    print('O triângulo é isósceles')
else:
    print('O triângulo é escaleno')