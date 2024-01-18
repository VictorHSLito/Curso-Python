# Estrutura Try e Except:

try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a/b
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados que você digitou")
except ZeroDivisionError:
    print("Você tentou dividr por zero!")
except KeyboardInterrupt:
    print("O usuário não digitou nada!")
except Exception as erro:
    print(f"O erro foi de {erro.__cause__}")
else:
    print(f"O resultado é {r:.1f}")
finally:
    print("Volte sempre!")
