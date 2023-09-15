n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break # Interrompe o laço de repetição
    s += n
print(f'A soma vale {s}')