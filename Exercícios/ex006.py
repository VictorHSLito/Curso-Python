'''# Arredondando um número

from math import trunc
num = float(input('Digite um valor:'))
print('O número digitado {} em sua forma inteira é: {}'.format(num, trunc(num)))'''

# Catetos e Hipotenusa
'''cat1 = float(input('Qual o comprimento do primero cateto? (em cm)'))
cat2 = float(input('Qual o comprimento do segundo cateto? (em cm)'))
hipo = (cat1**2 + cat2**2)**(1/2)
print('A hipotenusa desse triângulo vale: {}'.format(hipo))

import math
cat1 = float(input('Qual o comprimento do primero cateto? (em cm)'))
cat2 = float(input('Qual o comprimento do segundo cateto? (em cm)'))
hipo = math.hypot(cat1, cat2)
print('A hipotenusa vale: {}'.format(hipo))'''

# Seno, Cosseno e Tangente
'''import math
ang = float(input('Digite o ângulo aqui:'))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O seno desse ângulo vale {}\n O cosseno desse ângulo vale {}\n e a tangente desse ângulo vale {}'.format(sen, cos, tan))'''

# Sorteando um item na lista
'''import random
a1 = input('Digite o nome do Aluno:')
a2 = input('Digite o nome do segundo Aluno:')
a3 = input('Digite o nome terceiro Aluno:')
a4 = input('Digite o nome último Aluno:')
lista =[a1, a2, a3, a4]
print('O aluno sorteado foi:{}'.format(random.choice(lista)))'''

# Sorteando uma ordem na lista
'''from random import shuffle
a1 = input('Digite o nome do Aluno:')
a2 = input('Digite o nome do segundo Aluno:')
a3 = input('Digite o nome terceiro Aluno:')
a4 = input('Digite o nome último Aluno:')
lista =[a1, a2, a3, a4]
shuffle(lista)
print('A ordem sorteada é: {}'.format(lista))'''


