def dobro(arg):
    return arg*2


def triplo(arg):
    return arg*3

def metade(arg):
    return arg/2

def aumento(arg):
    return arg*1.1


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
