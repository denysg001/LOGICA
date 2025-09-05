"""
Escreva um algoritmo que leia dois números que deverão ser colocados,
respectivamente nas variáveis vA e vB.
O algoritmo deve, então, trocar os valores de vA por vB e vice-versa.
Mostrar o conteúdo destas variáveis conforme a ordem de digitação
antes da troca e após a troca.
"""
# ler dois números
vA = float( input("Digite o primeiro número: ") )
vB = float( input("Digite o segundo número: ") )

# mostrar as variáveis
print("vA=", vA, "vB=", vB)

# trocar os conteúdos
vA, vB = vB, vA
# aux = vA
# vA = vB
# vB = aux


# mostrar as variáveis
print("vA=", vA, "vB=", vB)






