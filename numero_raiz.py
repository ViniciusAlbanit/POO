n = int(input('n: '))
m1 = n // 100
m2 = n % 100
s = m1 + m2
q = s * s
if n == q:
    print('sim')
else:
    print('não')
