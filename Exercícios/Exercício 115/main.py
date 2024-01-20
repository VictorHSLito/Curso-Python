# Crie um pequeno sistema modularizado que permite cadastrar pessoas pelo seu nome e idade em um arquivo de txt simples
# O sistema vai ter somente duas opções: Cadastar uma nova pessoa e mostrar a listagem.

def menu():
    print(30*"-")
    print("MENU PRINCIPAL".center(30))
    print(30*"-")

    print("1 - Ver pessoas cadastradas\n"
          "2 - Cadastrar uma nova pessoa\n"
          "3 - Sair do programa")
    print(30 * "-")


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


menu()
opcao = int(input('Sua Opção: '))

if opcao == 1:
    lista()
elif opcao == 2:
    cadastrar()
else:
    finalizar()

print(30*"-")


