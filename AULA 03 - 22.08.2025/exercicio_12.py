"""
Desenvolva um algoritmo onde o usuário digite a distância, o consumo e o valor do litro de
combustível, com estes dados o algoritmo deverá calcular a quantidade de litros de combustível para a
viagem e o custo da viagem.
"""

distancia = float(input("Digite a distância da viagem em km: "))
consumo = float(input("Digite o consumo do carro em km/litro: "))
valor = float(input("Digite o valor do litro de combustível: "))

litros = distancia / consumo
custo = litros * valor

print(f"Quantidade de litros de combustível: {litros:.2f}") # o que é esse .2f?
print(f"Custo da viagem: R$ {custo:.2f}")
