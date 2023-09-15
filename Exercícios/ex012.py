#  Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

'''números = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez','Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('Digite um número entre 0 e 20: '))
if 0 <= num <= 20:
    print(f'Você digitou o número {números[num]}')
else:
    print('Por favor, leia a pergunta e tente novamente!')
while True:
    pergunta = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {números[num]}')
    else:
        print('Por favor, leia a pergunta e tente novamente!')'''

# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

'''import random

numeros = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
print('Os números sorteados foram: ', end='')
for i in numeros:
    print(f'{i}', end= ' ')
print(f'\nO maior deles foi {max(numeros)}')
print(f'O menor deles foi {min(numeros)}')'''

# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.

'''num = (int(input('Digite um número: ')), 
          int(input('Digite mais um número: ')), 
          int(input('Digite mais um número: ')),
          int(input('Agora digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 aparece na {num.index(3)+1} posição')
print('Os números pares digitados foram: ', end='')
for i in num:
    if i % 2 == 0:
        print(i, end=' ')'''

# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

'''tupla = ('Caderno', 16.00,
         'Lápis', 1.25,
         'Lapiseira', 15.99,
         'Régua', 7.99,
         'Borracha Simples', 2.50,
         'Planilha', 14.99)

print('-'*40)
print(f'{"Listagem de Preço":^40}')
print('-'*40)

for posicao in range(0, len(tupla)):
    if posicao % 2 ==0:
        print(f'{tupla[posicao]:.<30}', end='')
    else:
        print(f'R${tupla[posicao]:>7.2f}')

print('-'*40)'''

# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

'''palavras = ('Computador', 'Desenvolvedor', 'Programador', 'Hardware', 'Software', 'Python', 'JavaScript', 'Teclado', 'Mouse', 'Jogos')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} tem-se as vogais: ', end='')
    for vogal in palavra:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')'''


