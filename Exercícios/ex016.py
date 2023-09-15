# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

'''def area(larg, comp):
    área = larg*comp
    print(f'A área desse retângulo de {larg}cm largura e {comp}cm comprimento é de: {área} cm²')

while True:
    area(float(input('Qual o valor da largura desse retângulo? ')), float(input('Qual o valor do comprimento? ')))
    pergunta = str(input('Deseja calcula outra área [S/N]? ')).upper()[0]
    if pergunta == 'N':
        break'''

# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.


'''def special_print(arg):
    quant = len(arg) + 4
    print("-"*quant)
    print(f'  {arg}')
    print("-"*quant)


special_print(str(input("Digite alguma coisa: ")))'''

# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

'''print("-"*30)
print("Contagem de 1 até 10 de 1 em 1")
for i in range(1, 11, 1):
    time.sleep(0.5)
    print(i, end=' ')
print("Fim!")
print("-" * 30)
for c in range(10, -2, -2):
    time.sleep(0.5)
    print(c, end=' ')
print("Fim")
print("-" * 30)
print("Agora é sua vez de personalizar a contagem!")


def countador(início, fim, passo):
    if passo < 0:
        passo *= -1

    if início < fim:
        count = início
        while count <= fim:
            time.sleep(0.5)
            print(count, end=' ')
            count += passo
        print("Fim")
    else:
        count = início
        while count >= fim:
            time.sleep(0.5)
            print(count, end=' ')
            count -= passo
        print("Fim")


countador(int(input("Início: ")), int(input("Fim: ")), int(input("Passo: ")))'''

# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

'''def maior(* num):
    print("Analisando os valores...")
    print(f"Foram informados {len(num)} números, os quais são: ", end='')
    for i in list(num):
        print(f'{i}', end=' ')
    print()
    print(f"Dentre eles o maior valor foi de {max(num)}")

maior(-1, -2, -3, -4, -5, -20)'''

# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

números = list()


def sorteia():
    for i in range(0, 5):
        números.append(randint(0, 100))
    for num in números:
        print(f'{num}', end=' ')
    print("Pronto")


def somaPar():
    soma = 0
    print(f"Os valores pares da lista {números} são: ", end='')
    for i in números:
        if i % 2 == 0:
            soma += i
            print(f"{i}", end=' ')
    print()
    print(f"A soma desses valores é de {soma}")

print("Sorteando 5 valores para a lista: ", end='')
sorteia()
print("Somando os valores pares!")
somaPar()

