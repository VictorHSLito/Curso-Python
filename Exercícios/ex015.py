# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

'''dados = {'Nome': '', 'Média': ''}

dados["Nome"] = str(input('Qual o nome do aluno? '))
dados["Média"] = float(input('Qual a média desse aluno? '))

for k, v in dados.items():
    print(f'{k} do aluno é {v}')

if dados['Média'] >= 7:
    print('Esse aluno está Aprovado')
elif 5 <= dados['Média'] < 7:
    print('Esse aluno está de Recuperação')
else:
    print('Esse aluno está Reprovado')'''

# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

'''import random
from time import sleep
from operator import itemgetter

jogadores = dict()

for i in range(1, 5):
    jogadores[f'Jogador{i}'] = random.randint(1, 6)

for k, v in jogadores.items():
    print(f'{k} tirou {v}')
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)  # É possível também usar outra de sorted sem importar uma biblioteca.
# Usa-se o "key = lambda item: item[1], o "item[1]" faz com que a chave-parâmetro seja os valores tirados nos dados, caso fosse item[0] seria os jogadores

for i, c in enumerate(ranking):
    print(f'{i+1}° lugar - {c[0]} com {c[1]}')'''

# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

'''from datetime import datetime
dados = dict()

dados['Nome'] = str(input('Qual o nome da pessoa? '))
Nascimento = int(input('Que ano essa pessoa nasceu? '))
dados['Idade'] = datetime.now().year - Nascimento
dados['CTPS'] = int(input('Qual a Carteira de Trabalho? (Digite 0 caso não tenha) '))
if dados['CTPS'] != 0:
    dados['Ano_Contratação'] = int(input('Qual o ano de contratação? '))
    dados['Salário'] = float(input('Qual o salário? '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Ano_Contratação'] + 35) - datetime.now().year)

for k, v in dados.items():
    print(f'{k} = {v}')'''

# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

'''jogador = dict()

jogador['Nome'] = str(input('Digite o nome do Jogador: '))
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
jogador['Gols'] = list()

for i in range(0, jogador['Partidas']):
    jogador['Gols'].append(int(input(f'Quantos gols no jogo {i+1}? ')))

total = 0

for i in jogador['Gols']:
     total += i
     jogador['Total'] = total

print('='*30)
print(jogador)
print('='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')

print('='*30)

print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} jogos:')
for i, c in enumerate(jogador['Gols']):
    print(f'Na {i+1}ª partida fez {c} gols')
print(f'Foi um total de {jogador["Total"]} gols.')'''

# Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e o todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade
# C) Uma lista com mulheres D) Uma lista de pessoas com idade acima da média

'''lista = list()
dados = dict()
media_idade = 0

while True:
    dados['Nome'] = str(input('Qual o nome da pessoa? '))
    dados['Sexo'] = str(input('Qual o sexo dessa pessoa [M/F] ')).upper().strip()
    dados['Idade'] = int(input('Quantos anos ela tem? '))
    media_idade += dados['Idade']
    lista.append(dados.copy())
    dados.clear()
    pergunta = str(input('Deseja continuar [S/N]? ')).upper().strip()
    if pergunta == "N":
        break


print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'A média de idade foi de {media_idade/len(lista)}')
print('As mulheres cadastradas foram: ', end='')

for m in lista:
    if m['Sexo'] == 'F':
        print(f'{m["Nome"]}', end=' ')
print()

print(f'As pessoas com idade acima da média são: ', end='')

for i in lista:
    if i['Idade'] >= media_idade/len(lista):
        print('    ')
        for k, v in i.items():
            print(f'{k} = {v}; ', end='')
            print()'''

# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.  (REVISAR)

jogador = dict()
times = list()

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Digite o nome do Jogador: '))
    jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    jogador['Gols'] = list()

    for i in range(0, jogador['Partidas']):
        jogador['Gols'].append(int(input(f'Quantos gols no jogo {i+1}? ')))

    total = 0

    for i in jogador['Gols']:
         total += i
         jogador['Total'] = total

    times.append(jogador.copy())

    while True:
        pergunta = str(input('Deseja continuar [S/N]? ')).upper()[0]
        if pergunta in "SN":
            break
        print('Erro! Responda apenas Sim ou Não.')
    if pergunta == 'N':
        break

print('='*30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(times):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('='*30)

while True:
    busca = int(input('Dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca > len(times):
        print(f'Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENDO DO JOGADOR {times[busca]["Nome"]}:')
        for i, g in enumerate(times[busca]['Gols']):
            print(f'   No jogo {i+1} fez {g} gols')
print('='*30)
print('<<Encerrando o Progama>>')
