#Fazer um algoritmo para ler dois números e mostrar o maior deles

numero01 = float(input("Digite o primeiro número: "))
numero02 = float(input("Digite o segundo número: "))

if numero01 > numero02:
    print(f"O maior número é: {numero01}")
elif numero02 > numero01:
    print(f"O maior número é: {numero02}")
else:
    print(f"Os dois números são iguais: {numero01}")

