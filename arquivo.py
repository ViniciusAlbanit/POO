def gera_csv():
    with open('disciplina.csv', 'a') as arq:
        nome = input('Nome? ')
        while nome != '':
            trab = float(input('Trabalho? '))
            prova = float(input('Prova? '))
            rf = input('Reprovado por faltas? ')
            arq.write(f'{nome};{trab:.1f};{prova:.1f};{rf}\n')
            print('-' * 20)
            nome = input('Nome? ')

def le_csv():
    alunos = []
    with open('disciplina.csv', 'r') as arq:
        for linha in arq:
            linha = linha.rstrip()
            aluno = linha.split(';')
            aluno[1] = float(aluno[1])
            aluno[2] = float(aluno[2])
            if aluno[3] == 'sim':
                aluno[3] = True
            else:
                aluno[3] = False
            alunos.append(aluno)
    return alunos

#gera_csv()
alunos = le_csv()
for aluno in alunos:
    print(aluno)