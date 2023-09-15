# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa
# Retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

import time
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
print(f"Após as análises {nome}, concluímos que você tem {idade} anos e o voto esse ano é {voto(ano)}")