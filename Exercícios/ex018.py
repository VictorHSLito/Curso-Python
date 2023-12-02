# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

preço = float(input("Digite um preço: R$"))

'''print(f'A metade de R${preço} é {moeda.metade(preço)}')
print(f'O dobro de R${preço} é {moeda.dobro(preço)}')
print(f'O triplo de R${preço} é {moeda.triplo(preço)}')
print(f'O aumento de 10% de R${preço} é {moeda.aumento(preço)}')'''

# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado

print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'O triplo de {moeda.moeda(preço)} é {moeda.moeda(moeda.triplo(preço))}')
print(f'O aumento de 10% de {moeda.moeda(preço)} é {moeda.moeda(moeda.aumento(preço))}')
