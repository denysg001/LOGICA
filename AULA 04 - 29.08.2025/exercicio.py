n1 = int(input("Digite o 1º número: ")) # Lê o primeiro número
n2 = int(input("Digite o 2º número: ")) # Lê o segundo número

if n1 < n2: # Compara os números
    if n2 - n1 > 1:
        print (f"Os numeros entre {n1} e {n2} são: ")
        for i in range(n1 + 1, n2):
            print(i)
    else:
        print ("Não há números inteiros entre esses números")
elif n1 > n2: # Compara os números
    if n1 - n2 > 1:
       print (f"Os numeros entre {n1} e {n2} são: ")
       for i in range(n1 - 1, n2, -1):
           print(i)
    else:
       print (f"Não há números inteiros entre esses números")
else:
   print ("Os números são iguais")