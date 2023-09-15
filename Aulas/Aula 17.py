num = [2, 5, 9, 1]
num[2] = 3
num.append(7)  # Adiciona o valor 7 no final da lista
num.sort()  # Ordena a lista do menor para o maior
num.sort(reverse=True)  # Ordena a lista do maior para o menor
num.insert(2, 3)  # Adiciona o valor "3" na posição [2] da lista
num.pop()  # Remove o último valor da lista
num.pop(3)  # Remove o valor na posição [3] da lista
num.remove(2)  # Remove o primeiro valor "2" encontrado na lista, varrendo desde a posição 0 até encontrar o número  solicitado
if 8 in num:
    num.remove(8)
else:
    print('Não foi encontrado o número na lista')
print(num)
print(f'Essa lista tem {len(num)} elementos')

# Outra forma de criar uma lista

valores = []  # Pode-se usar também o comando 'list ()'
valores.append(4)
valores.append(3)
valores.append(9)

for valor in valores:
    print(valor)

# Outra forma de mostrar a lista com a posição de cada elemento

for posição, valor in enumerate(valores):
    print(f'Na posição {posição} encontrei o valor {valor}!')
print('Fim da lista')

# Copiar uma lista

a = [3, 2, 4, 5]
b = a[:]  # Copia todos os elementos de a, sem que crie uma ligação entre as listas, podendo assim fazer alterações desse tipo:
b[3] = 9
print(f'Lista A: {a}')
print(f'Lista B: {b}')
