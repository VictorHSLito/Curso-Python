'''if carro_esquerda():
    carro.siga()
elif carro_esquerda():
    carro.direita()
else:
    carro.siga()
    carro.esqueda()'''
nome = input('Digite seu nome aqui:')
lista = ['Victor', 'Tomy', 'Giovana']
if nome in lista:
    print('Que nome bonito!')
elif nome == 'João' or 'Pedro':
    print('Seu nome é bastante popular')
else:
    print('Seu nome é comum...')
print(f'Tenha um excelente dia {nome}!')
