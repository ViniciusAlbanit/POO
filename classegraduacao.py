class PosGraduacao():
    def __init__(self, instituicao, curso):
        self.instituicao = instituicao
        self.curso = curso

    def get_curso(self):
        pass # na subclasse a string 'doutorado em ' + nome do curso.

class Doutorado(PosGraduacao):
    def init(self, instituicao, curso, tese=None):
        super().__init__(instituicao, curso)
        self.__tese = tese

    def get_curso(self):
        return 'doutorado em ' + self.curso

    def get_tese(self):
        return self.tese

    def set_tese(self, titulo):
        self.__tese = titulo

d = Doutorado('USP', 'Ciência da Computação',
              'Argumentação Computacional')

print(d.get_tese())
        