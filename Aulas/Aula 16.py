lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita') # Os parênteses indicam que se trata de uma tupla
# Tuplas são imutáveis

'''for comida in lanche:
    print(f'Eu irei comer {comida}')
print('Comi muito bem!')'''

for count in range(0, len(lanche)):
    print(lanche[count])
print('Comi pra caramba!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')