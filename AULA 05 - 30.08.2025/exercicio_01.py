# Exercício 1
# Faça um algoritmo que leia uma frase e diga quantas 
# vogais existem na frase digitada.(considerar apenas AaEeIiOoUu)

frase = input("Digite uma frase: ")
vogais = "AaEeIiOoUu"
contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1

print(f"A frase '{frase}' possui {contador} vogais.")