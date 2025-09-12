# Exercício 4
# Faça um algoritmo que leia uma string no formato de data (dd/mm/aaaa)
# e escreva esta com o nome do mês por extenso.

def converter_data(): # Função que converte a data
    # Dicionário com os nomes dos meses
    meses = {
        '01': 'janeiro', '02': 'fevereiro', '03': 'março',
        '04': 'abril', '05': 'maio', '06': 'junho',
        '07': 'julho', '08': 'agosto', '09': 'setembro',
        '10': 'outubro', '11': 'novembro', '12': 'dezembro'
    }
    
    # Lê a data no formato dd/mm/aaaa
    data = input("Digite uma data (dd/mm/aaaa): ")
    
    # Separa os componentes da data
    dia, mes, ano = data.split('/') # split() divide a string em partes, usando '/' como separador
    
    # Obtém o nome do mês
    nome_mes = meses[mes]
    
    # Exibe a data formatada
    print(f"{dia} de {nome_mes} de {ano}")

# Executa o programa
converter_data() # explica o que está acontecendo aqui
# A função converter_data() é chamada para iniciar o processo de conversão da data.
# Quando chamamos a função, o código dentro dela é executado, permitindo que o usuário insira uma data e veja o resultado formatado.
# Isso é necessário porque definir a função apenas cria o bloco de código, mas não o executa.
# Sem essa chamada, nada aconteceria quando o script fosse executado.