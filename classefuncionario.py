class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def __repr__(self):
        return  f'Nome: {nome}\n' +\
                f'Salario: {self.aumentar_salario()}'
    
    def aumentar_salario(self):
        return (self.salario * percentual / 100) + self.salario 

nome = input('Seu nome: ')
salario_total = float(input('Qual o seu salário: '))
percentual = float(input('Qual a percentual do aumento do salário: '))
func = Funcionario(nome, salario_total)
print(func)
