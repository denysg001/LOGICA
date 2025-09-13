while True:
    print("Para encerrar o programa, digite 0 como primeiro número")
    n1 = int(input("Digite o 1º número: ")) # Lê o primeiro número
    if n1 == 0: # Verifica se o primeiro número é 0
        break # Sai do loop se for 0
    else:
        n2 = int(input("Digite o 2º número: ")) # Lê o segundo número
        print (f"A soma dos números é: {n1 + n2}") # Exibe a soma dos números
print ("Programa encerrado, voce digitou 0 como primeiro número") # Exibe mensagem de encerramento do programa
