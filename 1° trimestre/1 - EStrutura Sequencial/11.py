# 11) Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre:
# • O produto do dobro do primeiro com metade do segundo.
# • A soma do triplo do primeiro com o terceiro.
# • O terceiro elevado ao cubo.
n1 = int(input("digite o primeiro numero inteiro:"))# numero sem virgula ou negativo
n2 = int(input("digite o segundo numero inteiro:"))
n3 = float(input("digite o terceiro numero(real)"))# qualquer numero
print(f"dobro do primeiro com meteda do segundo: {((n2 /2 ) + (n1 * 2)):.2f}")
print(f"soma do triplo do primeiro com terceiro: {((n1 * 3) + n3):.2f}")
print(f"terceiro elevado ao cubo: {((n3 * n3)* n3):.2f}")