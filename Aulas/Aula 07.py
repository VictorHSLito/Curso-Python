# (+) Adição, (-) Subtração, (*) Multiplicação, (/) Divisão, (**) Exponenciação, (//) Divisão exata, (%) Resto da divisão.
## Ordem de procedência "()"; "**"; "*, /, //, %"; "+, -".
nome = input('Qual o seu nome?')
print('Prazer em te conhecer{}!'.format(nome))

##
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite o outro valor:'))
print('A soma desses números vale:{}'.format(n1+n2))
print('A multiplicação desses números vale:{}'.format(n1*n2)) 
print('A divisão entre esses números valem:{}'.format(n1/n2))
print('A soma exponencial desses números vale:{}'.format((n1*n1)+(n2*n2)))
print('O resto da divisão entre esses números vale:{}'.format(n1%n2))

###
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
s = n1 + n2
d =  n1/n2
m = n1*n2
print('A soma desses números é {},\n a divisão desses números é {}\n e a multiplicação desses números é {}'.format(s, d, m))
