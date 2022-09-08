class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def exibe(self):
        print ('Título: ', self.titulo)
        print('Autor: ', self.autor)
        print('Número páginas: ', self.num_paginas)
        print('-' * 20)

L1 = Livro('1984', 'George Orwell', 350)
L2 = Livro('Algoritimos: teorias e pratica', 'Thomas Corren', 1100)
L1.exibe()
L2.exibe()