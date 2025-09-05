#Ler 3 números e imprimi-los em ordem crescente.

numero01 = float(input("Digite o primeiro número: "))
numero02 = float(input("Digite o segundo número: "))
numero03 = float(input("Digite o terceiro número: "))  

if numero01 <= numero02 and numero01 <= numero03:
    if numero02 <= numero03:
        print(f"Números em ordem crescente: {numero01}, {numero02}, {numero03}")
    else:
        print(f"Números em ordem crescente: {numero01}, {numero03}, {numero02}")
elif numero02 <= numero01 and numero02 <= numero03:
    if numero01 <= numero03:
        print(f"Números em ordem crescente: {numero02}, {numero01}, {numero03}")
    else:
        print(f"Números em ordem crescente: {numero02}, {numero03}, {numero01}")
else:
    if numero01 <= numero02:
        print(f"Números em ordem crescente: {numero03}, {numero01}, {numero02}")
    else:
        print(f"Números em ordem crescente: {numero03}, {numero02}, {numero01}")




lista = []  # inicializa a lista
for x in range(3):  # repete 3 vezes
    n = float(input(f"Digite o {x+1}º número: "))  # lê o número
    lista.append(n)  # adiciona o número à lista
    print(lista)  # imprime a lista
    lista.sort()  # ordena a lista

print(f"Números em ordem crescente: {lista}")  # imprime a lista em ordem crescente