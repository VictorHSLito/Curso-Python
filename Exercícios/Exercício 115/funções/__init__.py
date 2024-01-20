def menu():
    print(30*"-")
    print("MENU PRINCIPAL".center(30))
    print(30*"-")

    print("1 - Ver pessoas cadastradas\n"
          "2 - Cadastrar uma nova pessoa\n"
          "3 - Sair do programa")
    print(30 * "-")

    while True:
        opção = leiaInt(input("Sua opção: "))
        if opção == 1:
            lista()
        elif opção == 2:
            cadastrar()
        else:
            return
        break


def lista():
    return


def cadastrar():
    print(30*'-')
    print("NOVO CADASTRO".center(30))
    print(30*'-')

    nome = str(input("Digite o nome da pessoa: "))
    idade = int(input("Digite a idade dessa pessoa: "))

    cadastro = list()
    cadastro.append(nome)
    cadastro.append(idade)
    print("Pessoa cadastrada com sucesso!")
    print(f'A pessoa {nome} e de idade {idade} foi cadastrada com sucesso no sistema!')


def finalizar():
    exit()


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