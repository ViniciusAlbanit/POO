class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
    
    def __repr__(self):
        return  f'Título: {self.titulo}\n' + \
                f'Autor:  {self.autor}\n' + \
                f'Número páginas:  {self.num_paginas}\n'  + \
                '-' * 20

L1 = Livro('1984', 'George Orwell', 350)
L2 = Livro('Algoritimos: teorias e pratica', 'Thomas Corren', 1100)
print(L1)