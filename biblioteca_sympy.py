from sympy import Symbol, symbols, factor, expand, pprint, Sum
a, b, c = symbols('a, b, c')
i = Symbol('i')
j = Symbol('j')
print(a + b + a + c + b + c)

a = Symbol('x')
print(a + a + 1)

a, b, c, x = symbols('a, b, c, x')
exp = a*x + b*x
print('Não faturada: ',exp)
print('Fatorada: ', factor(exp))
#expandida
a, b, c, x = symbols('a, b, c, x')
exp = a*x + b*x
fatorada = factor(exp)
expandida = expand(fatorada)
print('Não faturada: ',exp)
print('Fatorada: ', fatorada)
print('Expandida: ', expandida)
#pprint muda os sinais matematicos exemplo: * vira . Ele melhora a visão matematicamente
a, b, c, x = symbols('a, b, c, x')
exp = a*x + b*x
fatorada = factor(exp)
expandida = expand(fatorada)
print('Não faturada: ', end='')
pprint(exp)     
print('Fatorada: ', end='')
pprint(fatorada)
print('Expandida: ', end='')
pprint(expandida)

s = Sum(2*i, (i, 0, 5))
pprint(s)
Sum(s, (j, 10, 20))

#Ve a soma de algo, ai está a soma do s
print('Soma = ', s.doit())
