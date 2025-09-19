# Criando uma lista vazia
lista_vazia = []
print("Lista vazia:", lista_vazia)

# Criando uma lista com elementos
frutas = ["maçã", "banana", "laranja", "uva"]
print("Lista inicial:", frutas)

# 1. append() - Adiciona um elemento no final da lista
frutas.append("manga")
print("Após append('manga'):", frutas)

# 2. insert() - Insere elemento em uma posição específica
frutas.insert(1, "kiwi")  # Insere "kiwi" na posição 1
print("Após insert(1, 'kiwi'):", frutas)

# 3. remove() - Remove a primeira ocorrência do elemento
frutas.remove("banana")
print("Após remove('banana'):", frutas)

# 4. pop() - Remove e retorna elemento de uma posição (último se não especificar)
ultimo_elemento = frutas.pop()  # Remove o último
print("Elemento removido com pop():", ultimo_elemento)
print("Lista após pop():", frutas)

# 5. pop(index) - Remove elemento de posição específica
segundo_elemento = frutas.pop(1)
print("Elemento removido na posição 1:", segundo_elemento)
print("Lista após pop(1):", frutas)

# 6. index() - Retorna o índice da primeira ocorrência
posicao = frutas.index("laranja")
print("Posição de 'laranja':", posicao)

# 7. count() - Conta quantas vezes um elemento aparece
frutas.append("maçã")  # Adicionando maçã duplicada
quantidade = frutas.count("maçã")
print("Quantidade de 'maçã' na lista:", quantidade)

# 8. len() - Retorna o tamanho da lista
tamanho = len(frutas)
print("Tamanho da lista:", tamanho)

# 9. sort() - Ordena a lista em ordem crescente
frutas.sort()
print("Lista ordenada:", frutas)

# 10. reverse() - Inverte a ordem dos elementos
frutas.reverse()
print("Lista invertida:", frutas)

# 11. clear() - Remove todos os elementos da lista
lista_teste = ["a", "b", "c"]
print("Lista antes de clear():", lista_teste)
lista_teste.clear()
print("Lista após clear():", lista_teste)

# 12. extend() - Adiciona elementos de outra lista
frutas.extend(["pêra", "abacaxi"])
print("Após extend(['pêra', 'abacaxi']):", frutas)

# 13. copy() - Cria uma cópia da lista
copia_frutas = frutas.copy()
print("Cópia da lista:", copia_frutas)

# Acessando elementos por índice
print("\nAcessando elementos:")
print("Primeiro elemento:", frutas[0])
print("Último elemento:", frutas[-1])
print("Segundo ao quarto elemento:", frutas[1:4])

# Verificando se elemento existe na lista
if "maçã" in frutas:
    print("'maçã' está na lista")

# Iterando sobre a lista
print("\nIterando sobre a lista:")
for fruta in frutas:
    print(f"- {fruta}")

# Criando lista com range
numeros = list(range(1, 6))
print("\nLista de números:", numeros)

# List comprehension (criação de lista com condição)
pares = [x for x in range(10) if x % 2 == 0]
print("Números pares de 0 a 9:", pares)