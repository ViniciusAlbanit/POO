class PosGraduacao():
    def __init__(self, instituicao, curso):
        self.instituicao = instituicao
        self.curso = curso

    def get_curso(self, situacao):
        if situacao == 'Aprovado':
            return "Doutorado em " + self.curso
        else:
            return none

class Doutorado(PosGraduacao):
    def __init__(self, instituicao, curso, tese=None):
        super().init(instituicao, curso)
        self.__tese = tese

    def get_tese(self):
        return self.__tese

    def set_tese(self, titulo):
        self.__tese = titulo

    def repr(self):
        return (f'Instituição: {self.instituicao}\n' +
                f'Curso......: {self.curso}\n' +
                f'Tese.......: {self.__tese}')

d1 = Doutorado('Impacta', 'ADS')
print(d1.get_tese())
        