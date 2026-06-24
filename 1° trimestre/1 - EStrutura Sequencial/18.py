#18) Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de
# um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo
# usando este link (em minutos).
dados = int(input("digite quantida de dados a ser enviada(mb):"))
internet = int(input("digite a velocidade a internet(mbs):"))
segundos = (internet * 60) / dados  
print(f"tempo que ira levar é {(segundos / 60):.2f} minutos")
