# Em listas é possível criar uma lista dentro de outra

dados = ['João', 25]
pessoas = dados[:]   # Como já vimos anteriormente, esse comando cria uma cópia da lista "dados"
print(pessoas)

# Outra forma também seria:

dados = [['João', 25], ['Maria', 19], ['Luana', 14]]
print(dados[1][1])  # Mostra a idade "19" de "Maria"

for p in dados:
    print(f'{p[0]} tem {p[1]} anos de idade')


# Outra coisa interessante:
dado = list()
galera = list()
maior = menor = 0

for p in range (0,3):
    dado.append(str(input('Digite o seu nome: ')))
    dado.append(int(input('Digite sua idade')))
    galera.append(dado[:])
    dado.clear()  # Limpa a lista de dado

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1

print(f'Temos {maior} maiores de idade e {menor} menores de idades')