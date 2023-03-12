#Empréstimo Bancário
'''import time
valor_casa = float(input('Qual o valor da casa?'))
salario = float(input('Quanto é o salário da pessoa?'))
anos = int(input('Quantos anos irá pagar a casa?'))

prestacao_mensal = (valor_casa/anos)/12

print('Aguarde um momento, iremos conferir se o empréstimo poderá ser feito.')
time.sleep(4)

if prestacao_mensal == salario*0.3:
    print('Isso é 30% do seu salário, infelizmente você não pode financiar essa casa.')
elif prestacao_mensal < salario*0.3:
    print('Parabéns!!! O empréstimo será feito.')
else:
    print('Desculpe, mas não poderá ocorrer o empréstimo...')'''

#Conversor de bases
'''numero = int(input("Escreva um número inteiro:"))
menu = int(input('Agora escolha em qual base númerica gostaria de converter esse número: \n'
      '[ 1 ] Para base binária \n'
      '[ 2 ] Para base octal \n'
      '[ 3 ] Para base Hexadecimal \n'
      '[ 4 ] Para visualizar o número em todas as bases  \n '           
       'Digite aqui:'))

if menu == 1:
    print(f'O número {numero} na base binária é: {bin(numero)}')
elif menu == 2:
    print(f'O número {numero} na base octal é {oct(numero)}')
elif menu == 3:
    print(f'O número {numero} na base hexadecimal é {hex(numero)}')
elif menu == 4:
    print(f'O número {numero} na base binária é {bin(numero)}, na base octal é {oct(numero)} e na base hexadecimal é {hex(numero)}')
else:
    print('Erro! Escolha dentre uma das opção acima e tente novamente.')'''

#Comparador de números
'''num_1 = float(input('Digite o primeiro número:'))
num_2 = float(input('Digite agora o segundo número:'))
if num_1 > num_2:
    print(f'O número {num_1} é maior que o {num_2}')
elif num_1 == num_2:
    print('Os dois números são iguais!')
else:
    print(f'O número {num_2} é maior que o {num_1}')'''

#Alistamento militar
'''from datetime import date
sexo = int(input('Qual o seu sexo? Feminino ou Masculino \n'
                 '[ 1 ] Para o sexo feminino \n'
                 '[ 2 ] Para o sexo masculino \n'
                 'Escolha aqui:'))
if sexo == 1:
    print('Voce não precisa se alistar')
else:
    idade = int(input('Agora informe sua idade:'))
    nascimento = (date.today().year - idade)
    falta = int(18 - idade)
    passou = int(idade - 18)
    if idade < 18:
        print(f'Você nasceu no ano {nascimento} e agora tem {idade} anos. \nDesculpe mas ainda não é hora de se alistar, tente novamente faltam {falta} para poder se alistar.')
    elif idade == 18:
        print(f'Você nasceu no ano {nascimento} e agora tem {idade} anos \nQue boa notícia! Você já pode se alistar!')
    else:
        print(f'Você nasceu no ano {nascimento} e agora tem {idade} anos \nVish! O prazo de alistamento já se passou... Fazem mais de {passou} anos.')'''

#Média do aluno
'''nota_1 = float(input('Digite a primeira nota:'))
nota_2 = float(input('Digite a segunda nota:'))
media = (nota_1 + nota_2)/2
if 7 > media >=5:
    print(f'Infelizmente a sua média foi de {media} e você está recuperação...')
elif media < 5:
    print(f'A sua média foi de {media} e você está de reprovado')
else:
    print(f'Parabéns!!! A sua média foi de {media} e você está aprovado!')'''

#Categoria de Atletas
'''from datetime import date
import time
idade = int(input('Olá atleta! Quantos anos você tem?'))
nascimento = date.today().year - idade

time.sleep(1)

print(f'Você tem {idade} anos e nasceu no ano {nascimento}.')

if idade <= 9:
    print(f'Como você nasceu no ano {nascimento} e possui {idade} anos, você será colocado(a) na categoria MIRIM')
elif 9 < idade <= 14:
    print(f'Como você nasceu no ano {nascimento} e possui {idade} anos, você será colocado(a) na categoria INFANTIL')
elif 14 < idade <= 19:
    print(f'Como você nasceu no ano {nascimento} e possui {idade} anos, você será colocado(a) na categoria JÚNIOR')
elif 19 < idade <= 25:
    print(f'Como você nasceu no ano {nascimento} e possui {idade} anos, você será colocado(a) na categoria SÊNIOR')
else:
    print(f'Como você nasceu no ano {nascimento} e possui {idade} anos, você será colocado(a) na categoria MASTER')'''

#Analisador de triângulos
'''lado_1 = float(input('Qual o valor do primeiro lado?'))
lado_2 = float(input('Qual o valor do segundo lado?'))
lado_3 = float(input('Qual o valor do terceiro lado?'))
if lado_1 < lado_2 + lado_3 and lado_2 < lado_1 + lado_3 and lado_3 < lado_1 + lado_2:
    print('Esses lados podem formar um triângulo! ', end='')
    if lado_1 == lado_2 == lado_3:
        print('Esse triângulo é do tipo EQUILÁTERO!')
    elif lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
        print('Esse triângulo é do tipo ESCALENO!')
    else:
        print('Esse triângulo é do tipo ISÓCELES!')
else:
    print('Esses lados não podem formar um triângulo...')'''

#Cálculo IMC
'''peso = float(input('Qual o seu peso (em Kg)?'))
altura = float(input('Qual a sua altura (em m)?'))
imc = peso/(altura*altura)
if imc < 18.5:
    print(f'O seu IMC é de {imc} e você está ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print(f'O seu IMC é de {imc} e você está NO PESO IDEAL')
elif 25<= imc <30:
    print(f'O seu IMC é de {imc} e você está COM SOBREPESO')
elif 30 <= imc <40:
    print(f'O seu IMC é de {imc} e você está OBESO!')
else:
    print(f'O seu IMC é de {imc} e você está OBESIDADE MÓRBIDA!')'''

#Valor do produto e desconto
'''preço_produto = float(input('Informe o valor do produto:'))
dinheiro = preço_produto*0.9
cheque = preço_produto*0.9
cartao_avista = preço_produto*0.95
cartao_2x = preço_produto*1
cartao_3x = preço_produto*1.2

pagamento = int(input('Informe a forma de pagamento:\n'
                      '[1] Para pagamento em dinheiro ou cheque\n'
                      '[2] Para pagamento à vista no cartão\n'
                      '[3] Para pagamento no cartão em 2 parcelas\n'
                      '[4] Para pagamento no cartão em 3 ou mais parcelas\n'
                      'Escolha aqui:'))
if pagamento == 1:
    print(f'Você tem 10% de desconto com essa forma de pagamento, o novo preço do produto será de R${dinheiro}')
elif pagamento == 2:
    print(f'Você tem 5% de desconto com essa forma de pagamento, o novo preço do produto será de R${cartao_avista}')

elif pagamento == 3:
    print(f'Infelizmente essa forma de pagamento não possui desconto, o preço a se pagar será de R${cartao_2x}')
elif pagamento == 4:
    print(f'Devido a essa forma de pagamento possuir muitas parcelas, haverá um juros de 20% no preço do produto, resultando em um valor de R${cartao_3x}')
else:
    print('Por favor, escolha uma forma de pagamento dentre as opções listadas.')'''

#Jokenpo Game
'''import random
import time
escolha = int(input('Pronto para jogar Pedra, Papel e Tesoura? Escolha uma dentre as opções abaixo:\n'
                    '[1] Para Pedra\n'
                    '[2] Para Papel\n'
                    '[3] Para Tesoura\n'
                    'Sua escolha:'))

lista = [1, 2, 3]
computador = random.choice(lista)

print('Pronto?')
time.sleep(1)
print('JO', end='')
time.sleep(1)
print('KEN', end='')
time.sleep(1)
print('PO!!')
time.sleep(1)
print('-='*45)
if escolha == 1 and computador == 2:
    print('Você escolheu PEDRA e o computador escolheu PAPEL, O computador venceu!! Tente novamente.')
elif escolha == 1 and computador == 3:
    print('Você escolheu PEDRA e o computador escolheu TESOURA, PARABÉNS!! Você venceu!!')
elif escolha == 1 and computador == 1:
    print(f'Você escolheu PEDRA e o computador escolheu PEDRA, parece que temos um empate, tente novamente!')
elif escolha == 2 and computador == 1:
    print(f'Você escolheu PAPEL e o computador escolheu PEDRA, PARABÉNS!! Você venceu!!')
elif escolha == 2 and computador == 3:
    print(f'Você escolheu PAPEL e o computador escolheu TESOURA, O computador venceu!! Tente novamente.')
elif escolha == 2 and computador == 2:
    print(f'Você escolheu PAPEL e o computador escolheu PAPEL, parece que temos um empate, tente novamente!')
elif escolha == 3 and computador == 1:
    print(f'Você escolheu TESOURA e o computador escolheu PEDRA, O computador venceu!! Tente novamente.')
elif escolha == 3 and computador == 2:
    print(f'Você escolheu TESOURA e o computador escolheu PAPEL, PARABÉNS!! Você venceu!!')
elif escolha == 3 and computador == 3:
    print(f'Você escolheu TESOURA e o computador escolheu TESOURA, parece que temos um empate, tente novamente!')
else:
    print('Por favor escolha uma opção válida.')
print('-='*45)'''
