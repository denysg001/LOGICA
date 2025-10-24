meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

vendas = []

print("Digite o número de vendas para cada mês:")

venda_janeiro = int(input("Vendas de Janeiro: "))
vendas.append(venda_janeiro)

venda_fevereiro = int(input("Vendas de Fevereiro: "))
vendas.append(venda_fevereiro)

venda_marco = int(input("Vendas de Março: "))
vendas.append(venda_marco)

venda_abril = int(input("Vendas de Abril: "))
vendas.append(venda_abril)

venda_maio = int(input("Vendas de Maio: "))
vendas.append(venda_maio)

venda_junho = int(input("Vendas de Junho: "))
vendas.append(venda_junho)

venda_julho = int(input("Vendas de Julho: "))
vendas.append(venda_julho)

venda_agosto = int(input("Vendas de Agosto: "))
vendas.append(venda_agosto)

venda_setembro = int(input("Vendas de Setembro: "))
vendas.append(venda_setembro)

venda_outubro = int(input("Vendas de Outubro: "))
vendas.append(venda_outubro)

venda_novembro = int(input("Vendas de Novembro: "))
vendas.append(venda_novembro)

venda_dezembro = int(input("Vendas de Dezembro: "))
vendas.append(venda_dezembro)

total_vendas = venda_janeiro + venda_fevereiro + venda_marco + venda_abril + venda_maio + venda_junho + venda_julho + venda_agosto + venda_setembro + venda_outubro + venda_novembro + venda_dezembro

media_anual = total_vendas / 12

print() # linha em branco

print(f"A média anual foi {media_anual}.") 

meses_acima_media = 0

if vendas[0] > media_anual:
    print(f"Janeiro: {vendas[0]} vendas")
    meses_acima_media += 1

if vendas[1] > media_anual:
    print(f"Fevereiro: {vendas[1]} vendas")
    meses_acima_media += 1

if vendas[2] > media_anual:
    print(f"Março: {vendas[2]} vendas")
    meses_acima_media += 1

if vendas[3] > media_anual:
    print(f"Abril: {vendas[3]} vendas")
    meses_acima_media += 1

if vendas[4] > media_anual:
    print(f"Maio: {vendas[4]} vendas")
    meses_acima_media += 1

if vendas[5] > media_anual:
    print(f"Junho: {vendas[5]} vendas")
    meses_acima_media += 1

if vendas[6] > media_anual:
    print(f"Julho: {vendas[6]} vendas")
    meses_acima_media += 1

if vendas[7] > media_anual:
    print(f"Agosto: {vendas[7]} vendas")
    meses_acima_media += 1

if vendas[8] > media_anual:
    print(f"Setembro: {vendas[8]} vendas")
    meses_acima_media += 1

if vendas[9] > media_anual:
    print(f"Outubro: {vendas[9]} vendas")
    meses_acima_media += 1

if vendas[10] > media_anual:
    print(f"Novembro: {vendas[10]} vendas")
    meses_acima_media += 1

if vendas[11] > media_anual:
    print(f"Dezembro: {vendas[11]} vendas")
    meses_acima_media += 1

percentual = meses_acima_media * 100
percentual = percentual / 12

print()

print(f"O número de vendas que ficaram acima da média foi {percentual}%.")