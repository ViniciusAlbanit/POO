# Crie um programa que solicite ao usuário o nome e
# o número de cinco candidatos que concorrerão à uma
# eleição, o número deve ser único para cada candidato e
# serão válidos apenas números naturais.
# Em seguida, peça os votos de cada pessoa para que possam
# ser contabilizados, o voto será mediante o número do
# candidato.
# Ao final, o programa deverá exibir o nome dos candidatos,
# e a quantidade de votos, inclusive os votos em branco.
# O programa também deverá exibir o vencedor da eleição.
# Obs.(1): O programa deve prever a situação em que o usuário
#          tente votar em um candidato inexistente, nesse caso
#          o voto será anulado. Uma mensagem deverá ser exibida
#          indicando o ocorrido.
# Obs.(2): Caso o usuário digite o número de voto -1, isso indicará
#          um voto em branco. Uma mensagem deverá ser exibida
#          indicando o ocorrido.
# Obs.(3): Após a confirmação de um voto válido, o programa deverá
#          exibir o nome do candidato que recebeu o voto.
# Obs.(4): O programa deve registrar os números dos candidatos, os
#          nomes e a quantidade de votos em um dicionário, isto é,
#          o número deverá ser a chave e o valor associado uma lista
#          em que o primeiro valor é o nome e o segundo a quantidade
#          de votos.
# Obs.(5): O seu código de resposta deve estar logo em seguida deste
#          enunciado, ou seja, faça o download deste arquivo, insira
#          o seu código abaixo e anexe novamente o arquivo como resposta.




candidatos = {}
num_nome = 5
num_votos = 0
for _ in range(5):
    nome_cand = input(f'Digite o nomes do {num_nome} candidato: ')
    num_cand = int(input('Digite o número desse candidato: '))
    candidatos[num_cand] = [nome_cand, num_votos]
    num_nome -=1
    print()

print('-'*20)
print()
print(candidatos)
chave = candidatos.keys()
voto_branco = 0
for _ in range(5):
    print('Caso deseje votar em branco, digite -1')
    voto = int(input('Quais desses canditados você quer votar: '))
    if voto == -1:
        print('Voto em branco')
        voto_branco +=1
    elif voto not in candidatos:
        print(f'Voto inválido')
    else:
        print(candidatos[voto][0])
        candidatos[voto][1] += 1
print('-'*35)
print('Resultado')
print('-'*35)
for nome_cand, num_votos in candidatos.values():
    print(f'Nome do candidato: {nome_cand}')
    print(f'Quantidade de voto desse candidato: {num_votos}')
    print('-'*35)
resul = []
for votos in candidatos.values():
    resul.append(votos[1])
max_de_votos = max(resul)
for chaves in candidatos.values():
    if max_de_votos == chaves[1]:
        ganhador = chaves[0]
        break
print(f'Votos em branco: {voto_branco}')
print(f'O candidato eleito foi o: {ganhador}')

    