# Crie um pequeno sistema modularizado que permite cadastrar pessoas pelo seu nome e idade em um arquivo de txt simples
# O sistema vai ter somente duas opções: Cadastar uma nova pessoa e mostrar a listagem.
cadastro = []


def menu():
    while True:
        print(30 * "-")
        print("MENU PRINCIPAL".center(30))
        print(30 * "-")

        print("\033[33m1\033[m"" - " "\033[34mVer pessoas cadastradas\033[m\n"
              "\033[33m2\033[m" " - " "\033[34mCadastrar uma nova pessoa\033[m\n"
              "\033[33m3\033[m" " - " "\033[34mSair do programa\033[34m")
        print(30 * "-")

        opção = leiaInt("Sua opção: ")
        if opção == 1:
            lista()
        elif opção == 2:
            cadastrar()
        elif opção == 3:
            print("O programa será finalizado, obrigado")
            finalizar()
            break
        else:
            print("\033[31mOpção inválida! Tente novamente\033[m")


def lista():
    print(30 * '-')
    print("PESSOAS CADASTRADAS".center(30))
    print(30 * '-')
    lerarquivo()

    return


def cadastrar():
    print(30*'-')
    print("NOVO CADASTRO".center(30))
    print(30*'-')

    nome = str(input("Digite o nome da pessoa: "))
    idade = int(input("Digite a idade dessa pessoa: "))

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


def lerarquivo():
    try:
        a = open("pessoas.txt", 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.readlines())


menu()
