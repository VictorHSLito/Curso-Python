"""tempo = int(input("Quantos anos tem o seu carro?"))
if tempo <3:
    print('Seu carro está novo')
else:
    print('Seu carro não está novo')
print('--Fim--')"""

tempo = int(input("Quantos anos tem o seu carro?"))
print("Seu carro está novo" if tempo <3 else 'Seu carro está velho')
print('--Fim--')    