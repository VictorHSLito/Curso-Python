# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

'''temporaria = list()
pesadas = list()
leves = list()
principal = list()
contagem_pessoas = 0

while True:
    nome = str(input('Digite o nome da pessoa: '))
    peso = float(input('Agora digite o peso: '))
    temporaria.append(nome)
    temporaria.append(peso)
    if peso >= 100:
        pesadas.append(temporaria[:])

    elif peso <= 70:
        leves.append(temporaria[:])

    principal.append(temporaria[:])
    temporaria.clear()
    contagem_pessoas += 1
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if pergunta == "N":
        break

for peso in pesadas:
    maior_peso = peso[1]
    if peso[1] > maior_peso:
        maior_peso = peso[1]

for peso in leves:
    menor_peso = peso[1]
    if peso[1] < menor_peso:
        menor_peso = peso[1]
        
print(f'Foram cadastradas no total {contagem_pessoas} pessoas, {principal} ')

print(f'O maior peso foi de {maior_peso}, peso de ', end='')

for pess in principal:
    if pess[1] == maior_peso:
        print(f'{pess[0]}', end=' ')

print()

print(f'O menor peso foi de {menor_peso}, peso de ', end='')
for pess in principal:
    if pess[1] == menor_peso:
        print(f'{pess[0]}', end=' ')'''

# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

'''principal = list()

for i in range(1, 8):
    principal.append(int(input(f'Digite o {i}° valor: ')))
principal.sort()

print('Os valores pares dessa lista são:', end=' ')
for num in principal:
    if num % 2 == 0:
        print(num, end=' ')

print()

print('Já os valores ímpares são:', end=' ')

for num in principal:
    if num % 2 != 0:
        print(num, end=' ')'''

# Resolução do professor Guanabara:

'''num = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Todos os valores pares são: {num[0]}')
print(f'Todos os valores ímpares são: {num[1]}')'''

# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número na posição [{linha + 1}, {coluna + 1}]: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()'''

# Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.

'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_3_coluna = maior_valor = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número na posição [{l + 1}, {c + 1}]: '))
        if matriz[l][c] % 2 == 0:
            soma_pares = soma_pares + matriz[l][c]
        if c == 2:
            soma_3_coluna += matriz[l][c]
        if l == 1 and matriz[l][c] > maior_valor:
            maior_valor = matriz[l][c]

print(f'A soma dos valores pares dessa matriz é de {soma_pares}!')
print(f'A soma dos valores da terceira coluna é {soma_3_coluna}')
print(f'O maior valor da segunda linha vale {maior_valor}')'''

# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# MINHA RESOLUÇÃO:

'''import random


principal = list()
temp = list()

pergunta = int(input('Quantos palpites serão? '))

for c in range(0, pergunta):
    for i in range(0, 6):
        temp.append(random.randint(1, 60))
    temp.sort()
    principal.append(temp[:])
    temp.clear()

print(f'Foram feitos {pergunta} palpites, os quais são: ')

for indice, num in enumerate(principal):
    print(f'Jogo {indice + 1}: {num})'''

# RESOLUÇÃO DO PROFESSOR:

'''import random

principal = list()
temp = list()
total = 0

pergunta = int(input('Quantos palpites serão? '))

while total < pergunta:
    count = 0
    while True:
        num = random.randint(1, 60)
        if num not in temp:
            temp.append(num)
            count += 1
        if count >= 6:
            break
    temp.sort()
    principal.append(temp[:])
    temp.clear()
    total += 1

print(f'Foram gerados {pergunta} palpites, os quais são: ')

for i, p in enumerate(principal):
    print(f'Jogo {i+1}: {p}')'''

# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

'''dados = list()
temp = list()


while True:
    temp.append(str(input('Por favor, digite o nome do aluno(a): ')))
    temp.append(float(input('Qual a nota desse aluno na 1ª matéria? ')))
    temp.append(float(input('E na 2ª matéria? ')))
    dados.append(temp[:])
    temp.clear()
    pergunta = str(input('Deseja continuar cadastrando?[S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break

for i, c in enumerate(dados):
    media = (c[1] + c[2])/2
    print(f'{i}  Nome: {c[0]}  Média: {media}')

while True:
    nota = int(input('Gostaria de ver a nota de qual aluno?(999 para nenhum) '))
    if nota == 999:
        break
    print(f'O aluno(a) {dados[nota][0]} tirou as notas {dados[nota][1]}, {dados[nota][2]}')'''

