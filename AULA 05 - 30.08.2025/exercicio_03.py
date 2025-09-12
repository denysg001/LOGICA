# Exercício 3
# Faça um algoritmo que leia um texto e diga quantas 
# palavras existem neste texto.

# Lê o texto do usuário
texto = input("Digite um texto: ")

# Conta as palavras usando split() que separa por espaços
palavras = texto.split()
quantidade_palavras = len(palavras) # len() é uma função que retorna o tamanho (número de elementos) de um objeto, como uma lista.

# Exibe o resultado
print(f"O texto contém {quantidade_palavras} palavras.")