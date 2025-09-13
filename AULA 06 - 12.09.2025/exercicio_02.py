while True:
    n1 = int(input("Digite o 1º número: ")) # Lê o primeiro número
    n2 = int(input("Digite o 2º número: ")) # Lê o segundo número

    if n1 >= 30 and n1 <= 80 and n2 >= 30 and n2 <= 80: # Verifica se ambos os números estão no intervalo de 30 a 80
        if n1 < n2:
            while n1 < n2: # Loop para imprimir os números de n1 a n2
                print(n1) # Imprime o número atual
                n1 += 1 # Incrementa n1 em 1
        else:
            while n1 > n2: # Loop para imprimir os números de n1 a n2
                print(n1) # Imprime o número atual
                n1 -= 1 # Decrementa n1 em 1
    else:
        print("Números fora do intervalo de 30 a 80, digite novamente.") # Mensagem de erro se os números estiverem fora do intervalo