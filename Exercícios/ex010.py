# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

'''sexo = str(input("Digite o seu sexo [M/F]: ")).strip().upper()[0]
print(sexo)
while sexo not in 'MmFf':
    sexo = str(input("Dados inválidos, por favor informe o seu sexo: ")).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')'''

# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

'''import random
numeros = [0, 1, 2, 3 , 4 , 5, 6 , 7 , 8, 9, 10]
escolha = int(random.choice(numeros))
palpites = 1
print('Tente adivinhar o número que pensei de 0 a 10')
print('Pensei em um número, em quantas tentativas você acha que levará para acertar?')
resposta = int(input('Qual é o seu palpite: '))
while resposta != escolha:
    resposta = int(input('Parece que não foi dessa vez, tente outro palpite:'))
    palpites += 1
if resposta == escolha:
        print(f'Parabéns, você acertou depois de {palpites} palpites')'''

# Melhore o jogo do DESAFIO 28 onde o computador (Guanabara)

'''from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue acertar qual foi?')
palpites = 0
acertou = False

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')

print(f'Acertou!! Com um total de {palpites} tentativas')'''

# Criando um menu de opções

'''import time

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Agora digite outro valor: '))
sair = False

while not sair:
    time.sleep(1)
    print(50*'=-')
    menu = int(input(("""Por favor selecione uma das opções abaixo: \n
[1] Somar os dois números \n
[2] Multiplicar os dois números \n
[3] Comparar os dois números \n
[4] Digitar novos dois números \n
[5] Sair do programa \n
Sua escolha: """)))
    print(50*'=-') 
    if menu == 1:
        somar = (valor1 + valor2)
        print(f'A soma dos números é igual a {somar}')
    elif menu == 2:
        multiplicar = (valor1*valor2)
        print(f'A multiplicação desses dois números é igual a {multiplicar}')
    elif menu == 3:
        if valor1 > valor2:
            print(f'O maior valor entre esses dois números é: {valor1}')
        else:
            print(f'O maior valor entre esses dois números é: {valor2}')
    elif menu == 4:
        valor1 = int(input('Digite um novo valor: '))
        valor2 = int(input('Agora digite outro novo valor: '))
    elif menu == 5:
        sair = True
    else:
        print('Opção inválida, tente novamente')


print('Encerrando o programa...')
time.sleep(1)
print('Progama encerrado.')'''

# Faça um programa que leia um número qualquer e mostre o seu fatorial.  (Revisar)

'''numero = int(input('Digite um número: '))
contador = numero
fatorial = 1
print(f'O fatorial de {numero} é: ' , end='')

while contador > 0:
    fatorial = fatorial*contador
    contador = contador - 1
print(fatorial)'''

# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

'''numero = int(input('Digite o primeiro termo: '))
razao = int(input('Agora digite a razão: '))
contador = 1
print(f'Os 10 primeiros termos dessa P.A são: {numero}', end= '')

while not contador == 10:
    numero += razao
    contador += 1
    print(numero, end = '')'''

# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos. (Revisar)

'''numero = int(input('Digite o primeiro termo: '))
razão = int(input('Agora digite a razão: '))
termo = numero
count = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while count <= total:
        print(termo, end= ' ')
        termo = termo + razão
        count += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais gostaria de ver? '))
print('Fim do programa!')'''

# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

'''# [a1, a2, a3, a4, a5, ...] 0, 1, 1, 2, 3, 5, 8
# a3 = a2 + a1
# a4 = a3 + a2 
quant = int(input('Quantos termos gostaria de ver? '))
while quant != 0:
    aux = 0
    t1 = 0
    t2 = 1
    while not aux == quant:
        aux += 1
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        print(t3, end=' ')
    quant = int(input('Digite 0 caso não queira ver nenhum \n'
                      'Quantos termos gostaria de ver? '))
    if quant == 0:
        print('Fim do Programa.')'''

# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

'''num = 0
count = 0
soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    count += 1
    soma = soma + num
    num = int(input('Digite um número [999 para parar]: '))
print (f'Você digitou {count} números e a soma entre eles é {soma}!')'''

# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

'''num = int(input('Digite um número: '))
maior = menor = num
soma = num
count = 1
pergunta = str(input("Quer continuar? [S/N]: ")).strip().upper()
while pergunta != "N":
    num = int(input('Digite um número: '))
    if num > maior:
        maior = num
    elif  num < menor:
        menor = num
    count += 1
    soma = (soma + num)
    pergunta = str(input("Quer continuar? [S/N]: ")).strip().upper()
media = (soma/count)
print(f'Fim do programa, foram digitados {count} números e a média entre eles foi de {media} o maior número foi {maior} e o menor {menor}')'''