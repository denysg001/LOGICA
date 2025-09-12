# Exercício 2
# Faça um algoritmo que leia um texto com até 20 caracteres, 
# e imprima esse texto de traz para frente.

# Lê o texto do usuário
texto = input("Digite um texto (até 20 caracteres): ")

# Verifica se o texto tem até 20 caracteres
if len(texto) <= 20:
    # Imprime o texto de trás para frente
    texto_invertido = texto[::-1]
    print(f"Texto invertido: {texto_invertido}")
else:
    print("Erro: O texto deve ter no máximo 20 caracteres!")