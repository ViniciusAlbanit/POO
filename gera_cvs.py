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

gera_csv()