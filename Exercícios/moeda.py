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