# Desafio 2
# Crie um código que imprima o triangulo abaixo.
# lendo a quantidade de linhas.

linhas = int(input("Digite a quantidade de linhas: "))

for i in range(1, linhas + 1):
    espacos = " " * (linhas - i)
    hashes = "#" * i
    print(espacos + hashes)