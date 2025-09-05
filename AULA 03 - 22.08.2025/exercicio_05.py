# Ler um conjunto de 5 dados numéricos e imprimir sua soma e média

numero01 = float(input("Digite o primeiro número: "))
numero02 = float(input("Digite o segundo número: "))
numero03 = float(input("Digite o terceiro número: "))
numero04 = float(input("Digite o quarto número: "))
numero05 = float(input("Digite o quinto número: "))

soma = numero01 + numero02 + numero03 + numero04 + numero05
media = soma / 5
print(f"A soma dos números digitados é: {soma} \n E a media é: {media}")


soma = 0 # inicializa a variável soma com 0
for i in range(1, 6): # i vai assumir os valores 1, 2, 3, 4, 5
    numero = float(input(f"Digite o {i}º número: ")) # solicita o número
    soma += numero # soma = soma + numero
media = soma / 5 # calcula a média
print(f"A soma dos números digitados é: {soma}") # imprime a soma
print(f"A média dos números digitados é: {media}") # imprime a média
