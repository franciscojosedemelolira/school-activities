# 13) Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu
# peso ideal, utilizando as seguintes fórmulas:
# • Para homens: (72.7*h) - 58
# • Para mulheres: (62.1*h) – 44.7
altura = int(input("digite sua altura:"))
print(f"seu peço ideal se você for homen é {((72.7 * altura) -58):.2}")
print(f"seu peço ideal se você for mulher é {((62.1* altura) -44.7):.2}")