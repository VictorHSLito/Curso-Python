# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais
# Informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108
'''import moeda

preço = float(input("Digite um preço: R$"))

print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço, True)}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço, True)}')
print(f'O triplo de {moeda.moeda(preço)} é {moeda.triplo(preço, True)}')
print(f'O aumento de 10% de {moeda.moeda(preço)} é {moeda.aumento(preço, True)}')
print(f'Reduzindo 12% de {moeda.moeda(preço)} é {moeda.diminuir(preço, 12, True)}')'''

# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo()
# Que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui

import moeda

preço = float(input("Digite um preço: R$ "))
moeda.resumo(preço)