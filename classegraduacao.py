class PosGraduacao():
    def __init__(self, instituicao, curso):
        self.instituicao = instituicao
        self.curso = curso

    def get_curso(self, situacao):
        pass

class Doutorado(PosGraduacao):
    def __init__(self, instituicao, curso, tese=None):
        super().init(instituicao, curso)
        self.__tese = tese

    def get_curso(self):
        return 'doutorado em ' + self.curso

    def get_tese(self):
        return self.tese

    def set_tese(self, titulo):
        self.__tese = titulo

    def repr(self):
        return (f'Instituição: {self.instituicao}\n' +
                f'Curso......: {self.curso}\n' +
                f'Tese.......: {self.__tese}')

d1 = Doutorado('Impacta', 'ADS', 'Argumentação')
print(d1.get_tese())
        