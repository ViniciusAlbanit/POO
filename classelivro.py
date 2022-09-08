class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

def exibe(L):
    print ('Título: ', L.titulo)
    print('Autor: ', L.autor)
    print('Número páginas: ', L.num_paginas)
    print('-' * 20)

L1 = Livro('1984', 'George Orwell', 350)
L2 = Livro('Algoritimos: teorias e pratica', 'Thomas Corren', 1100)
exibe(L1)
exibe(L2)