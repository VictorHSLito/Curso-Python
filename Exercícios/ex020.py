# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(arg):
    while True:
        try:
            n = int(input(arg))
        except (ValueError, TypeError):
            print("\033[31mERRO: Por favor, digite um número válido!\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mEntrada de dados interrompida pelo usuário!\033[m")
            return None
        else:
            return n

def leiaFloat(arg):
    while True:
        try:
            n = float(input(arg))
        except (ValueError, TypeError):
            print("\033[31mERRO: Por favor, digite um número válido!\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mEntrada de dados interrompida pelo usuário!\033[m")
            return None
        else:
            return n
n1= leiaInt("Digite um número: ")
n2 = leiaFloat("Digite um número real: ")
print(f"Você digitou o número {n1} e o real foi {n2}")