# Parâmetros opcionais

def somar(a = 0, b = 0, c = 0):  # Colocando os parâmetros igual a 0, eles se tornam opcionais
    soma = a + b + c
    if soma == 0:
        print("A soma vale 0, pois não foram passados argurmentos ou todos os valores são 0")
    else:
        print(f"A soma vale {soma}")


somar()

# Escopo de Variáveis


def teste():
    x = 8  # A variável "X" só tem valor na função, sendo ela uma variável LOCAL
    print(f"Na função teste, n vale {n}")
    print(f"Na função teste, x vale {x}")


# Programa principal
n = 2  # "N" é uma variável GLOBAL
print(f"No programa principal, n vale {n}")
# print(f"No progama principal, x vale {x}")
teste()

# Retorno de valores


def somar(a = 0, b = 0, c = 0):
    soma = a + b + c
    return soma  # A instrução "return" toma um valor que está em uma função e o envia de volta à linha que a chamou


r1 = somar(1, 2 ,3)
r2 = somar(3, 4)
r3 = somar(5, 5, 5)

print(f"Os valores das somas foram: {r1}, {r2} e {r3}.")
