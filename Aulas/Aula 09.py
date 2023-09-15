# Fatiamento (Pegar "pedaços" da string)

frase = 'Curso de Python'

frase[4] # Mostra apenas a string n° 4 da frase

frase[4:14] # Começa da string n° 4 e vai até a string n° 13 (Sempre 1 a menos no final)

frase[4:14:2] # Começa da string n° 4 e vai até a string n° 13, porém pulando de 2 em 2

frase[:5] # Começa da primeira string e termina na string n° 4

frase[5:] # Começa da string n° 5 e termina até o final da string

frase[9::3] # Começa da string n° 9, vai até o final, pulando de 3 em 3

# Análise de Strings

len(frase) # Mostra a quantidade de caracteres na frase

frase.count('o') # Conta a quantidade de um caractere específico na frase

frase.count('o', 0, 13) # Conta a quantidade de um caractere específico na frase começando da string 0 até a string 12

frase.find('urso') # Indica em que posição se encontra a expressão digitada, no caso em qual string ela começa

frase.find('Android') # Caso a expressão não seja encontrada na frase, retornará o valor -1, indicando que não foi encontrada.

'Curso' in frase # O operador "in" vai indicar se aquele conjunto de caracteres existe na frase, apenas indicando com True ou False

# Transformação de Strings

frase.replace('Python', 'Android') # Troca a palavra 'Python' por 'Android' na frase

frase.upper() # Coloca toda a frase em letras Maiúsculas

frase.lower() # Coloca toda a frase em letras Minúsculas

frase.capitalize() # Coloca todos os caractéres em MINÚSCULO, porém com o primeiro caractere em MAIÚSCULO

frase.title() # Faz com que todas as palavras tenham o primeiro caractere em MAIÚSCULO

frase.strip() # Remove todos os espaços inúteis no início e no fim da frase

frase.rstrip() # Remove somente os últimos espaços da frase

frase.lstrip() # Remove apenas os primeiros espaços da frase

# Divisão de Strings

frase.split() # Vai ocorrer uma divisão das strings, considerando os espaços vazios como parâmetro para a divisão, dividindo a string em uma lista

# Junção de Strings

'-'.join(frase) # Vai juntar todos os elementos da frase usando o separador '-' como parâmetro

