#15) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no
# mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11%
# para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# • Salário bruto, quanto pagou de IR e ao INSS, quanto pagou ao sindicato e o salário líquido.
#• Calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto: R$
# - IR (11%): R$
# - INSS (8%): R$
# - Sindicato (5%): R$
# = Salário Líquido: R$
# Obs.: Salário Bruto - Descontos → Salário Líquido.
ganho = int(input("digite quanto você ganha por hora:"))
hora =  int(input("digite quantas horas foram trabalhadas neste mês:"))
salario_bruto = ganho * hora
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (ir + inss + sindicato)

print(f"""
>>>>> RELATORIO <<<<<
salario.bruto...: R${salario_bruto}
IR.(11%)........: R${ir}
INSS.(8%).......: R${inss}
Sindicato.......: R${sindicato}
Salario.liquido.: R${salario_liquido}
""")