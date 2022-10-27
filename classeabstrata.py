from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def exibir_nome(self):
        pass

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def exibir_nome(self):
        print('Nome do funcionário:', self.nome)

class Aluno(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def exibir_nome(self):
        print('Nome do aluno:', self.nome)

f = Funcionario('João', 25, 1500.00)
a = Aluno('Pedro', 19, 'Programação')