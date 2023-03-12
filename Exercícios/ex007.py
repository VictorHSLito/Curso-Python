#Custo da Viagem
'''quilometragem = float(input('Quantos quilômetros foi a sua viagem?'))
preço_1 = quilometragem*0.50
preço_2 = quilometragem*0.45
if quilometragem <= 200:
    print('O custo da sua viagem foi de:{}'.format(preço_1))
elif quilometragem > 200:
    print('O total a se pagar pela viagem é de:'.format(preço_2))

print('Obrigado e volte sempre!')'''

#Custo da Viagem (Outra forma)
'''quilometragem = float(input('Quantos quilômetros foi a sua viagem?'))
preço = quilometragem*0.50 if quilometragem <= 200 else quilometragem*0.45
print('O preço de sua viagem foi de: {}, Obrigado e volte sempre!'.format(preço))'''

#Ano Bissexto
'''ano = int(input('Qual ano quer analisar?'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano é Bissexto')
else:
    print('Esse ano não é Bissexto')'''

#Maior e menor valor
'''valor_1 = float(input('Digite um número:'))
valor_2 = float(input('Digite outro número:'))
valor_3 = float(input('Digite mais um número:'))
menor = valor_1
if valor_3 < valor_1 and valor_3 < valor_2:
    menor = valor_3
if valor_2 < valor_1 and valor_2 <valor_3:
    menor = valor_2    
if valor_1 > valor_2 and valor_1 > valor_3:
    print('O {} é o maior número! E {} é o menor.'.format(valor_1, menor))
if valor_2 > valor_1 and valor_2 > valor_3:
   print('O {} é o maior número! E {} é o menor.'.format(valor_2, menor))
if valor_3 > valor_2 and valor_3 > valor_1:
    print('O {} é o maior número! E {} é o menor.'.format(valor_3, menor))
if valor_1 == valor_2 and valor_1 == valor_3:
    print("Todos os números são iguais.")'''

#Aumentos múltiplos
'''salario = float(input('Qual o seu salário?'))
if salario > 1250:
    aumento = salario*1.10
    print('O seu aumento será de {}'.format(aumento))
else:
    aumento = salario*1.15
    print('O seu aumento será de {}'.format(aumento))'''
