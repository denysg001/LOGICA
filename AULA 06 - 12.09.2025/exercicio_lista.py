lista = [1, 12, 3, 4, 5, 3, 2]

print("""
Manipulando uma lista
===================================================
1- Adicionar um número na lista
2- Retirar um elemento da lista
3- Retirar um elemento da lista pelo índice
4- Localizar a posição de um elemento da lista
5- Inserir um elemento em uma posição específica
6- Excluir todos elementos da lista
7- Mostrar os elementos da lista ordenados
8- Escolha um elemento e mostre quantos existem
9- sair
""")

while True:
    print(f"\nLista atual: {lista}")
    opcao = input("Escolha uma opção (1-9): ")
    
    if opcao == "1":
        numero = int(input("Digite o número para adicionar: "))
        lista.append(numero)
        print(f"Número {numero} adicionado!")
        
    elif opcao == "2":
        if lista:
            elemento = int(input("Digite o elemento para remover: "))
            if elemento in lista:
                lista.remove(elemento)
                print(f"Elemento {elemento} removido!")
            else:
                print("Elemento não encontrado na lista!")
        else:
            print("Lista está vazia!")
            
    elif opcao == "3":
        if lista:
            indice = int(input(f"Digite o índice (0 a {len(lista)-1}): "))
            if 0 <= indice < len(lista):
                elemento = lista.pop(indice)
                print(f"Elemento {elemento} removido da posição {indice}!")
            else:
                print("Índice inválido!")
        else:
            print("Lista está vazia!")
            
    elif opcao == "4":
        elemento = int(input("Digite o elemento para localizar: "))
        if elemento in lista:
            posicao = lista.index(elemento)
            print(f"Elemento {elemento} encontrado na posição {posicao}")
        else:
            print("Elemento não encontrado na lista!")
            
    elif opcao == "5":
        posicao = int(input(f"Digite a posição (0 a {len(lista)}): "))
        if 0 <= posicao <= len(lista):
            elemento = int(input("Digite o elemento: "))
            lista.insert(posicao, elemento)
            print(f"Elemento {elemento} inserido na posição {posicao}!")
        else:
            print("Posição inválida!")
            
    elif opcao == "6":
        lista.clear()
        print("Todos os elementos foram removidos!")
        
    elif opcao == "7":
        if lista:
            lista_crescente = lista.copy()
            lista_crescente.sort()
            print(f"Ordem crescente: {lista_crescente}")
            
            lista_decrescente = lista.copy()
            lista_decrescente.sort(reverse=True)
            print(f"Ordem decrescente: {lista_decrescente}")
        else:
            print("Lista está vazia!")
            
    elif opcao == "8":
        elemento = int(input("Digite o elemento para contar: "))
        quantidade = lista.count(elemento)
        print(f"O elemento {elemento} aparece {quantidade} vez(es) na lista")
        
    elif opcao == "9":
        print("Saindo...")
        break
        
    else:
        print("Opção inválida! Escolha entre 1 e 9.")