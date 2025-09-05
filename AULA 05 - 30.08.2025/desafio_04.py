# Desafio 4
# Crie um código que imprima o retângulo abaixo.
# lendo a quantidade de linhas e colunas.
# Utilize o comando for

# Lê as dimensões do retângulo
linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))

for i in range(linhas):
    for j in range(colunas):
        # Primeira e última linha
        if i == 0 or i == linhas - 1:
            print("#", end="")
        # Segunda e penúltima linha
        elif i == 1 or i == linhas - 2:
            if j == 0 or j == colunas - 1:
                print("#", end="")
            else:
                print(" ", end="")
        # Linhas do meio
        else:
            if j == 0 or j == colunas - 1:
                print("#", end="")
            elif j == 2 or j == colunas - 3:
                print("#", end="")
            else:
                print(" ", end="")
    print()  # Nova linha