#17) Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros
# quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6
# litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3
# situações:
# • Comprar apenas latas de 18 litros;
# • Comprar apenas galões de 3,6 litros;
#• Misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
# sempre arredonde os valores para cima, isto é, considere latas cheias.
import math
area = int(input("digite a area quadrada a ser pintada:"))
desejo = int(input("""
1 - lata 18L = R%80
2 - galões 3,6L = R$25
3 - misturar os dois
>>>"""))

litros = area / 3
baldes = math.ceil(litros / 18)
galão = math.ceil(litros / 3.6)


if desejo == 1: # lata
    valor = baldes * 80
    galão = 0 
elif desejo == 2: #galão
    valor = galão * 25
    baldes =0
elif desejo == 3: #ambos
    baldes = math.floor(litros / 18)
    sobrante = (baldes / 18) * 18
    galão = math.ceil(sobrante / 3.6)
    valor = (( galão * 25) + (baldes * 80))


print(f"""
>>>relatorio<<<
litros: {litros:.2f}
bandes: {baldes:.0f}
galões: {galão:.0f}
valor: R${valor:.2f}
""")