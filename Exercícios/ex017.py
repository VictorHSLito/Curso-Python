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


def fatorial(num, mostrar=''):
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


print(fatorial(5, True))