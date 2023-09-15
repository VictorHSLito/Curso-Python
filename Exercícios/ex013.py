# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

'''lista = []
maior = menor = 0
for pos in range (0, 5):
    lista.append(int(input(f'Digite um valor na posição {pos}: ')))
    if pos == 0:
        maior = menor = lista[pos]
    else:
        if lista[pos] > maior:
            maior = lista[pos]
            posiçãomaior = pos
        elif lista[pos] < menor:
            menor = lista[pos]
            posiçãomenor = pos
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} e ele está na posição ', end='')
for posição, valor in enumerate(lista):
    if valor == maior:
        print(f'{posição}...', end='')
print()
print(f'O menor valor digitado foi {menor} e ele está na posição ', end='')
for posição, valor in enumerate(lista):
    if valor == menor:
        print(f'{posição}...', end='')
print()'''

# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

'''lista = []

while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        print('Valor adicionado com sucesso!')
        lista.append(num)
    else:
        print('Valor duplicado, não foi adicionado!')
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break
print(f'Os valores que você colocou na lista são {lista} e a lista em ordem crescente é', end='')
lista.sort()
print(lista)'''

# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

'''lista = []

for i in range (0,5):
    num = int(input('Digite um número: '))
    if i == 0 or num > lista[len(lista)-1]:
        lista.append(num)
    else:
        posição = 0
        while posição < len(lista):
            if num <= lista[posição]:
                lista.insert(posição, num)
                break
            posição += 1
print(lista)'''

# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:  A) Quantos números foram digitados.  B) A lista de valores, ordenada de forma decrescente.  C) Se o valor 5 foi digitado e está ou não na lista.

'''lista = []
count = 0

while True:
    num = (int(input('Digite um número: ')))
    lista.append(num)
    count += 1
    pergunta = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break

lista.sort(reverse=True)

if 5 in lista:
    x = 'aparece'
else:
    x = 'não aparece'

print(f'Foram digitados {count} números, a lista na forma decrescente é {lista} e o valor 5 {x}')'''

# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

'''lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    pergunta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break

pares = []
impares = []

for valor in lista:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)


print(f'A lista inicial é {lista} a lista apenas dos números pares é {pares} e a lista apenas dos números ímpares é {impares}')'''

# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

'''expressao = str(input('Digite sua expressão: '))
pilha = []

for parêntese in expressao:
    if parêntese == '(':
        pilha.append('(')
    elif parêntese == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está incorreta!')'''

# Outra forma de resolver o exercício acima

'''expressao = str(input('Digite sua expressão: '))

if expressao.count('(') == expressao.count(')'):
    print('Sua expressão é válida!')
else:
    print('Sua expressão está incorreta!')'''



