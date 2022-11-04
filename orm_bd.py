import sqlalchemy
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

engine = sqlalchemy.create_engine('sqlite:///server.db')
connection = engine.connect()

Base = declarative_base(engine)

session = Session()
connection.execute('''CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                      ID INTEGER PRIMARY KEY,
                      NOME VARCHAR(255) NOT NULL,
                      IDADE INT NOT NULL,
                      SALARIO FLOAT NOT NULL)''')
class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    idade = Column('IDADE', Integer)
    salario = Column('SALARIO', Float)

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
func = Funcionario('Zezinho', 20, 1700.00)
session.add(func)
session.commit()

func1 = Funcionario('Luizinho', 22, 1250.00)
func2 = Funcionario('Huguinho', 22, 2000.00)
lista = [func1, func2]
session.add_all(lista)
session.commit()
