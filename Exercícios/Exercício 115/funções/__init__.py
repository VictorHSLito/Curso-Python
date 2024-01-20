
def menu():   # Função que repetirá o Menu ao fim de cada interação
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
            opc2()
        elif opção == 3:
            print("O programa será finalizado, obrigado")
            finalizar()
            break
        else:
            print("\033[31mOpção inválida! Tente novamente\033[m")


def lista():   # Função que mostrará a lista de pessoas no arquivo txt já cadastradas
    print(30 * '-')
    print("PESSOAS CADASTRADAS".center(30))
    print(30 * '-')
    lerArquivo()
    return


def opc2():   # Função que cadastrará um novo registro no arquivo txt
    print(30*'-')
    print("NOVO CADASTRO".center(30))
    print(30*'-')

    nome = str(input("Digite o nome da pessoa: "))
    idade = leiaInt("Digite a idade dessa pessoa: ")
    cadastrar('pessoas.txt', nome, idade)


def finalizar():  # Função que finaliza o programa após o opção 3 ser escolhida
    exit()


def leiaInt(arg):  # Função auxiliar que obriga o usuário à digitar um número inteiro
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


def lerArquivo():  # Função que irá manipular os dados no arquivo txt
    try:
        a = open("pessoas.txt", 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()

def cadastrar(arq, nome='Sem nome', idade=0):   # Função responsável por cadastrar novos usuários no arquivo txt
    try:
        a = open(arq, 'at')
    except:
        print("Houve um erro ao cadastrar!")
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print("Houve um erro ao escrever o arquivo!")
        else:
            print(f"Novo registro de {nome} cadastrado")
            a.close()