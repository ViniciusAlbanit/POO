def quociente(a, b):
    return a // b

while True:
    print()
    try:
        x = int(input('x?'))
        y = int(input('b?'))
        print(f'{x} // {y} = {quociente(x , y)}')
    except:
        print('Ocorreu uma exceção')
    else:
        print('A operação pode ser executada')
        
    finally:
        continua = input('\nContinua [s/n]?')
        if continua ==  'n':break

print('Até Breve')
    
