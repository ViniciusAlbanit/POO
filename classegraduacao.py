class PosGraduacao():
    def __init__(self, instituicao, curso):
        self.instituicao = instituicao
        self.curso = curso
    def get_curso(self):
        self.curso
class Doutorado(PosGraduacao):
    def __init__(self, instituicao, curso, tese):
        super().__init__(instituicao, curso)
        self.__tese = None
    def get_tese(self):
        self.__tese
    def set_tese():
        