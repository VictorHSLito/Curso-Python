# Contagem Regressiva
'''from time import sleep
for i in range (10, -1, -1):
    print(i)
    sleep(1)
print('BOOOOM!! BOOM! POW!')'''

# Números Pares
'''n = 0
for i in range (0, 25):
    n = n + 2
    print(n, end=' ')

for g in range(2, 51, 2):
    print(g, end=' ')
print('Fim')'''

# Soma dos Números Ímpares e divisíveis por 3
'''soma = 0
contador = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma = soma + i
        contador = contador + 1
print(f'A soma dos {contador} números é de {soma}!')'''

# Tabuada 2.0v (minha forma)
'''n = int(input('Qual o número gostaria de ver a tabuada?'))
for i in range(n, n*10 +1):
    if i % n == 0:
        print(i)'''

# Tabuada 2.0v (professor):
'''num = int(input('Digite aqui o número que gostaria de ver a tabuada:'))
for c in range(1,11):
    print(f'{num} x {c} = {num*c}')'''

# Soma de Números Pares
'''soma = 0
cont = 0
for i in range(1,7):
    numero =int(input(f'Digite o {i}° número:'))
    if numero % 2 == 0:
        soma = soma + numero
        print(f'O resultado da soma é {soma}')
    cont = i 
print(f'Foram contados {cont} números e a soma total dos pares foi de {soma}')'''

# Somatório de uma PA
'''print('='*40)
print(' '*8, 'SOMATÓRIO DE UMA PA', ' '*8)
print('='*40)
razao = int(input('Digite o valor da razão: '))
num = int(input('Agora digite o valor do primeiro termo: '))
fim = int(input('Até qual n gostaria de somar? '))
for i in range (num, razao, fim):
    an = num + (fim -1)*razao
soma = ((num + an)*razao)/2
print(soma)'''

# 10 Termos de uma PA
'''print('='*40)
print(' '*8, 'TERMOS DE UMA PA', ' '*8)
print('='*40)
num = int(input('Digite o primeiro termo: '))
raz = int(input('Digite agora a razão: '))
a10 = (num + (9)*raz)
print('O termos da PA são:', end= ' ')
for i in range(num, a10 +raz, raz):
    print(f'{i}', end=' ')'''

# Números Primos
'''num = int(input('Digite aqui um número:'))
tot = 0
for i in range (1, num+1):
    if num % i == 0:
        tot += 1
        print('\033[33m', end='')
    else:
          print('\033[31m', end='')
    print(f'{i}', end=' ')
print(f'O número {num} foi divísivel {tot} vezes')
if tot == 2:
     print('E por isso esse número é primo')
else:
     print('Esse número não é primo')'''

# Detector de Palíndromo
'''frase = str(input('Digite aqui a frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''
for letra in range(len(juntar)-1, -1, -1):
    inverso += juntar[letra]
print(f'O inverso de {juntar} é {inverso}')
if inverso == juntar:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo')'''

# Detector de Palíndromo (Outra forma)
'''frase = str(input('Digite aqui a frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = juntar[::-1]
print(f'O inverso de {juntar} é {inverso}')
if inverso == juntar:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo')'''

# Grupo da Maioridade
'''from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for i in range(1, 8):
  ano = int(input(f'Em qual ano a {i}ª pessoa nasceu? '))
  idade = atual - ano
  if idade > 21:
    totmaior += 1
  else:
    totmenor += 1
print(f'Ao todos tivemos {totmaior} pessoas maiores de idade e {totmenor} pessoas menores de idade!')'''

# Maior e menor da sequência
'''maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input(f'Qual o peso da {i}ª pessoa? '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi de {maior} e o menor peso foi de {menor}.')'''

# Analisador completo
somadasidades = 0
mediaidade = 0
homemvelho = ''
idadehomem = 0
totmulher20 = 0
for pessoas in range(1, 5):
    print(5*'-', f'{pessoas}ª Pessoa', 5*'-')
    nome = str(input('Nome: ')).strip()
    Idade = int(input('Idade: '))
    Sexo = str(input('Sexo [M/F]: ')).strip()
    somadasidades = somadasidades + Idade
    if pessoas == 1 and Sexo in 'Mm':
        homemvelho = nome
        idadehomem = Idade
    if Sexo in 'Mm' and Idade > idadehomem:
        homemvelho = nome
        idadehomem = Idade
    if Sexo in 'Ff' and Idade <20:
        totmulher20 += 1
mediaidade = somadasidades/4
print(f'O homem mais velho se chama {homemvelho} e tem {idadehomem} anos')
print(f"A média das idades foi de {mediaidade} anos")
print(f'O número de mulheres menores de 20 anos foi de {totmulher20}')