# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa
# Retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

'''import time
import datetime

def voto(ano):
    if idade >= 18:
        return "OBRIGATÓRIO"
    elif 16 <= idade < 18:
        return "OPCIONAL"
    else:
        return "NEGADO"


nome = str(input("Qual o seu nome? "))
print(f"Olá {nome}, poderia me informar seu ano de nascimento? ", end='')
ano = int(input())
data_atual = datetime.datetime.now()
ano_atual = data_atual.year
idade = ano_atual - ano
print("Iremos ver agora se você tem idade suficiente para votar ou não")
print("Aguarde um instante")
time.sleep(2)
voto(ano)
print(f"Após as análises {nome}, concluímos que você tem {idade} anos e o voto esse ano é {voto(ano)}")'''

# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular
# E outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


'''def fatorial(num, mostrar=''):
    """
    Calcula o Fatorial de um número
    :param num: Para o fatorial do número ao ser calculado
    :param mostrar: Para mostrar a multiplicação ou não
    :return: Retorna o resultado
    """
    fat = 1
    for i in range(num, 0, -1):
        if mostrar:
            print(f"{i}", end='')
            if i > 1:
                print(" x ", end='')
            else:
                print(" = ", end='')
        fat = fat*i
    return fat


print(fatorial(5, True))'''

# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

'''def ficha(nome='<não informado>', gols = 0):
    print(f"O jogador {nome} fez {gols} gols(s) durante o campeonato.")


jogador = str(input("Qual o nome do jogador? "))
quant = str(input("Quantos gols ele fez? "))

if quant.isnumeric():
    quant = int(quant)
else:
    quant = 0

if jogador.strip() == "":
    ficha(gols=quant)
else:
    ficha(jogador, quant)'''

# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do Python
# Só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(arg):
    validação = False
    valor = 0
    while True:
        n = str(input(arg))
        if n.isnumeric():
            valor = int(n)
            validação = True
        else:
            print("Por favor digite um número")
        if validação:
            break
    return valor

n = leiaInt("Digite um número: ")
print(f"Você digitou o número {n}")