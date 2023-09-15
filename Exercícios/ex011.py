# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

'''num = 0
soma = 0
count = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    count += 1
    soma += num
print(f'Você digitou {count} números e a soma entre eles foi de {soma}.')'''

# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa deverá ser interrompido pelo usuário quando o número solicitado for negativo

'''num = 0
while num >= 0:
    num = int(input('\nDigite um número para ver a tabuada [Digite qualquer número negativo para parar]: '))
    count = 1
    if num <0:
        break
    while count != 11:
        multiplicação = num*count
        count += 1
        print(multiplicação, end=' ')
print('Acabou!')'''
#Solução do guanabara:
'''while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    if n <0:
        break
    print('-'*30)
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('Acabou!')'''

# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

'''from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in "PI":
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            v += 1
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            v += 1
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {v} vezes')'''

#  Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.

'''h = f =  i = 0
pessoas = 0
while True:
    print('='*10,'CADASTRE UMA PESSOA', '='*10)
    idade = int(input('Qual a idade? '))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input('Qual o sexo? [M/F] ')).strip().upper()[0]
    pessoas += 1
    if sexo == 'M':
        h += 1
    if idade >= 18:
        i += 1
    elif sexo == "F" and idade <= 20:
        f += 1
    pergunta = ' '
    while pergunta not in "SN":
        pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break
print(f'O total de pessoas cadastradas foram de {pessoas}, dentre eles {i} pessoas tem mais de 18 anos, {h} são homems e {f} são mulheres com menos de 20 anos.')'''    

# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.

'''print('='*30)
print('{:^30}'.format('Banco DEV'))
print('='*30)
valor = int(input('Quanto você gostaria de sacar? R$ '))
total = valor
ced = 50
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'O total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced ==20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break

print('='*30)
print('Volte sempre ao Banco DEV! Tenha um bom dia!')'''

