#explique o for e o range
# for = para
# range = alcance, intervalo
# range(inicio, fim, passo)
# range(fim) -> começa em 0, vai até fim-1, pulando de 1 em 1
# range(inicio, fim) -> começa em inicio, vai até fim-1, pulando de 1 em 1
# range(inicio, fim, passo) -> começa em inicio, vai até fim-1, pulando de passo em passo
#Exemplos:
# Repete 5 vezes, de 0 a 4
for i in range(5):
    print(i)
# Saída:
# 0
# 1
# 2
# 3

# Começa em 2, vai até 8, pulando de 2 em 2
for i in range(2, 10, 2):
    print(i)
# Saída:
# 2
# 4
# 6 
# 8
# Fim dos exemplos
# --- IGNORE ---

# outros exemplos de for e range e explicações

# for i in range(3): # i vai assumir os valores 0, 1, 2
#     print(f"Valor de i: {i}")
#     for j in range(2): # j vai assumir os valores 0, 1
#         print(f"  Valor de j: {j}")
#     print("Fim do loop interno")
# print("Fim do loop externo")
# Saída:
# Valor de i: 0
#   Valor de j: 0
#   Valor de j: 1
# Fim do loop interno
# Valor de i: 1
#   Valor de j: 0
#   Valor de j: 1
# Fim do loop interno
# Valor de i: 2
#   Valor de j: 0
#   Valor de j: 1
# Fim do loop interno
# Fim do loop externo
# --- IGNORE ---
# for i in range(1, 6): # i vai assumir os valores 1, 2, 3, 4, 5
#     print(f"Contador: {i}")
# Saída:
# Contador: 1
# Contador: 2
# Contador: 3
# Contador: 4
# Contador: 5   
# --- IGNORE ---

soma = 0
for i in range(1, 6): # i vai assumir os valores 1, 2, 3, 4, 5
    numero = float(input(f"Digite o {i}º número: "))
    soma += numero

media = soma / 5
print(f"A soma dos números digitados é: {soma}")
print(f"A média dos números digitados é: {media}")  
