class ContaBancaria:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.__saldo = saldo
    
    def __repr__(self):
        return (f'Número da conta: {self.numero}\n' +
                f'Titular........: {self.titular}\n' +
                f'Saldo..........: R$ {self.__saldo:.2f}\n')

    @property
    def saldo(self):
        senha = input('Senha? ')
        if senha == '123':
            return self.__saldo
        else:
            return None

    @saldo.setter
    def saldo(self, valor):
        if valor <= 2*self.__saldo:
            self.__saldo = valor
        else:
            print('Operação suspeita!')

c1 = ContaBancaria(123, 'João', 5000.00)
#saldo = c1.get_saldo(senha)
saldo = c1.saldo
if saldo == None:
    print('Acesso não autorizado!')
else:
    print('Saldo:', saldo)
    #c1.set_saldo(2 * saldo)
    c1.saldo = 2 * saldo
    saldo = c1.saldo
    print('Saldo:', saldo)