# Funções

def soma(a, b):       # Funções são como "rotinas", são executadas sempre que chamadas.
    s = a + b         # Sendo as vezes necessário definir um parâmetro ou não.
    print(s)


soma(4, 5)
soma(8, 4)
soma(30, 30)


def contador(* num):
    quant = len(num)
    print(f'Recebi os valores {num} e são ao todo {quant}')


contador(1, 2, 3, 4, 5)
contador(4, 2, 3, 1, 5, 6)


def dobrar(lista):
    pos = 0
    while pos < len(valores):
        lista[pos] *= 2
        pos += 1


valores = [1, 4, 2, 5, 9]
dobrar(valores)
print(valores)