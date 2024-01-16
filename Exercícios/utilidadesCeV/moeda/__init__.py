def dobro(arg, formato=False):
    res = arg*2
    return res if not formato else moeda(res)


def triplo(arg, formato=False):
    res = arg * 3
    return res if not formato else moeda(res)


def metade(arg, formato=False):
    res = arg/2
    return res if not formato else(res)


def aumento(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if not formato else moeda(res)


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def diminuir(preço, arg, formato= False):
    res = preço * (1 - arg/100)
    return res if not formato else moeda(res)

def resumo(preço=0, taxa_a=10, taxa_r=5):
    print('-' * 30)
    print("RESUMO DO VALOR".center(30))
    print('-'*30)
    print(f'Preço analisado: {moeda(preço)}')
    print(f'Dobro do preço: {dobro(preço, True)}')
    print(f'Metade do preço: R${metade(preço, True)}')
    print(f'Com {taxa_a}% de aumento: {aumento(preço, taxa_a,True)}')
    print(f'Com {taxa_r}% de redução: {diminuir(preço, taxa_r, True)}')
    print('-'*30)