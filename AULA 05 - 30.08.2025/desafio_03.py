# Desafio 3
# Crie um código que imprima o triangulo abaixo.
# lendo a quantidade de linhas.

linhas = int(input("Digite a quantidade de linhas: "))

for i in range(linhas):
    espacos = " " * (linhas - i - 1)
    hashtags = "#" * (2 * i + 1)
    print(espacos + hashtags)