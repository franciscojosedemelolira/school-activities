
import json
with open("bancodedados.json", "r") as carregamento:
    contas = json.load(carregamento)
conta_logada = None
from datetime import datetime

def salvar_dados():
    print("informação salva")
    with open("bancodedados.json", "w") as arquivo:
        json.dump(contas, arquivo, indent= 4, ensure_ascii= False)

def menu():
    while True:
        while True:
            print(f"""
        ===================
        existem {len(contas)} usuarios cadastrados""")
            print("""
        ======= MENU =======
        1 - Criar conta
        2 - Entrar em conta
        3 - lista de contas
        4 - procurar por cpf
        5 - encerrar programa
        ====================
        """)
            try:
                escolha = int(input(">>>"))
            except ValueError:
                print("insira valor valido")
                continue

            if escolha in (1,2,3,4,5):
                break

        if escolha == 1: #criar conta
            criar_conta()

        elif escolha == 2: #entrar em uma conta
            entrar_conta()

        elif escolha == 3: #lista de contas
            lista_usuarios()

        elif escolha == 4: # procurar cpf
            procurar_por_cpf()

        elif escolha == 5:
            print("obrigado por entrar na nossa agencia, tenha um bom dia")
            exit()
def procurar_por_cpf():
    global contas

    usuario_desejado = input("digite o cpf da pessoa desejada:")
    for desejado in contas:
        if usuario_desejado == desejado["cpf"]:
            print("usuario encontrado")
          
            for tag, info in desejado["info_conta"].items():
                print(f"{tag}: {info}")
            return
    print("usuario não encontrado")
    return
def criar_conta(): # criando conta
    global contas
    while True:
        cpf = input("digite seu cpf:")
        nome = input("digite seu nome:")

        while True:# verificação de senha igual
            try:
                senha = int(input("digite sua senha(somente numeros):"))
            except:
                print("erro de senha, deve ser somente numero")
                continue
            try:
                senhateste = int(input("digite sua senha novamente:"))
            except:
                print("senha deve ser somente numero")
                continue

            if senha == senhateste:
                usuario = procurar_conta_por_cpf(cpf)
                if usuario == None:
                    contas.append({"cpf": cpf ,"limitesaque": 0,"ultimo_saque": "",
                    "limitedeposito": 0,"ultimo_deposito": "","extrato": [],
                    "info_conta": {
                    "data_criação": datetime.now().strftime("%d/%m/%Y"),
                    "quantida_login": 0,
                    "nome":nome,"senha": senha,
                    "saldo": 0,
                    }})
                    salvar_dados()

                    print("conta criada com sucesso!")
                    return
                else:
                    print("ja existe um usuario com este cpf")
                    return
            else:
                print("!as duas senha devem ser iguais!")
def lista_usuarios():
    for usuario in contas:
        print(usuario["info_conta"]["nome"])
    return
def entrar_conta():
    global conta_logada
    while True:
        cpf = input("digite seu cpf:")
        senha = int(input("digite sua senha:"))
        usuario_logado = procurar_conta_por_cpf(cpf)

        if usuario_logado == None:
            print("usuario inexistente!")
            return
            
        if senha != usuario_logado["info_conta"]["senha"]:
            print("senha incorreta")
            return

        conta_logada = usuario_logado
        conta_logada["info_conta"]["quantida_login"] += 1
        conta_logada["info_conta"]["ultimo_login"] = datetime.now().strftime("%d/%m/%y")
        print(f"você logou em {usuario_logado}")
        salvar_dados()
        break

    menu_bancario()

def opção_conta():
    global conta_logada
    while True:
        escolha = int(input("""
    === opção de conta ===
    1 - excluir conta
    2 - alterar nome
    3 - alterar senha
    4 - extrato 
    5 - info de conta
    6 - sair 
    ======================
     >>>"""))
        if escolha == 1: #excluir conta
            excluir_conta()
            return

        elif escolha == 2: # alterar nome
            alterar_nome()
            return

        elif escolha == 3: #alterar senha
            alterar_senha()
            return

        elif escolha == 4: # extrato
            for item in conta_logada["extrato"]:
                print(f"""
 ====================
 tipo: {item["tipo"]}
 data: {item["data"]}
 hora: {item["hora"]}
 valor: {item["valor"]}""")
                if item["pessoa"] != None:
                    print(f""" pessoa:{item["pessoa"]}""")
                if item["chave_pix"] != None:
                    print(f""" chave:{item["chave_pix"]}""")
                print(""" ====================""")
                return
        elif escolha == 5: # ver informações da conta
            for chave , valor in conta_logada["info_conta"].items():
                print(f"{chave}: {valor}")
            return
        elif escolha == 6: # sair
            print("saindo da conta")
            conta_logada = None
            return
def excluir_conta():

    escolha = int(input("""
    você reamente deseja excluir sua conta?
    1 - sim
    2 - não 
    >>>"""))
    if escolha == 1:
        print("você é louco!")
        contas.remove(conta_logada)
        salvar_dados()
    return
def alterar_nome():
    while True:
        novo_nome1 = input("digite seu novo nome:")
        novo_nome2 = input("digite seu novo nome novamente:")

        if novo_nome2 != novo_nome1:
            print("os dois nomes devem ser iguais!")

        else:
            conta_logada["info_conta"]["nome"] = novo_nome1
            salvar_dados()
            return
def alterar_senha():
    while True:
        nova_senha1 = int(input("digite sua nova senha:")) 
        nova_senha2 = int(input("digite sua nova senha novamente:")) 

        if nova_senha1 != nova_senha2:
            print("as duas senha devem ser iguais!")

        else:
            conta_logada["info_conta"]["senha"] = nova_senha1
            salvar_dados()
            return

def menu_bancario():
    global conta_logada
    if conta_logada == None:
        return
    else:
        while True:
            escolha = int(input(f"""
        ==== MINHA CONTA ====
        nome: {conta_logada["info_conta"]["nome"]}
        saldo: {conta_logada["info_conta"]["saldo"]}
        numero de logins: {conta_logada["info_conta"]["quantida_login"]}
        === MENU BANCARIO ===
        1 - consultar saldo
        2 - depositar
        3 - sacar
        4 - transferir
        5 - pix
        6 - opção de conta
        =====================
        >>>"""))
            if escolha == 1: # consultar saldo
                consultar_saldo()

            elif escolha == 2: # depositar
                depositar()

            elif escolha == 3: # sacar
                sacar()

            elif escolha == 4: # transferir
                transferir()

            elif escolha == 5:
                area_pix()

            elif escolha == 6: # opção de conta
                opção_conta()
                if conta_logada == None:
                    break
        return
def consultar_saldo():
    tipo = "consulta"

    print(f"seu saldo atual é : {conta_logada["info_conta"]["saldo"]}")

    conta_logada["extrato"].append({
    "tipo": tipo,
    "data": datetime.now().strftime("%d/%m/%y"),
    "hora": datetime.now().strftime("%H/%M/%S")
    })
    salvar_dados()
    return
def depositar():
    tipo = "depositar"
    if conta_logada["limitedeposito"] >= 3:
        if conta_logada["ultimo_deposito"] != datetime.now().strftime("%d/%m/%y"):
            conta_logada["limitedeposto"] = 0
        else:
            print("você ja alcançou seu limite diario de depositos")
            return

    else:
        deposito = int(input("qual valor você deseja depositar?:"))

        if deposito < 0:
            print("você não pode depositar valor negativo")

        else:
            conta_logada["extrato"].append({   
    "tipo": tipo,
    "data": datetime.now().strftime("%d/%m/%y"),
    "hora": datetime.now().strftime("%H/%M/%S"),
    "valor": deposito
    })
            conta_logada["info_conta"]["saldo"] += deposito
            conta_logada["limitedeposito"] += 1
            conta_logada["ultimo_deposito"] = datetime.now().strftime("%d/%m/%y")
            salvar_dados()
    return
def sacar():
    tipo = "saque"
    if conta_logada["limitesaque"] >= 3:
        if conta_logada["ultimo_saque"] != datetime.now().strftime("%d/%m/%y"):
            conta_logada["limetesaque"] = 0
        else:
            print("você ja alcançou seu limite de saques")
            return
    else:
        saque = int(input("digite o quanto quer sacar:"))

        if saque > conta_logada["info_conta"]["saldo"]:
            print("você não possui esse valor em conta")

        elif saque < 0:
            print("você não pode sacar valor negativo")

        else:
            conta_logada["extrato"].append({
    "tipo": tipo,
    "data": datetime.now().strftime("%d/%m/%y"),
    "hora": datetime.now().strftime("%H/%M/%S"),
    "valor": - saque
            })
            conta_logada["info_conta"]["saldo"] -= saque
            conta_logada["limitesaque"] += 1
            conta_logada["ultimo_saque"] = datetime.now().strftime("%d/%m/%y")
            salvar_dados()
    return
def transferir():
    tipo = "transferencia"
    global contas
    destinatario = input("digite o cpf de quem deseja transferir:")
    cpf_destinatario = procurar_conta_por_cpf(destinatario)
    if cpf_destinatario == None:
        print("usuario inexistente!")
        return

    if cpf_destinatario["cpf"] == conta_logada["cpf"]:
        print("você não pode transferir para si mesmo")
        return

    elif cpf_destinatario["cpf"] == destinatario:
        destinatario = cpf_destinatario
        print("usuario existente")
        valor = int(input("quanto deseja transferir para esse pessoa?:"))

        if valor < 0:
            print("você não pode transferir valor negativo")
            return

        elif valor > conta_logada["info_conta"]["saldo"]:
            print("você não possui saldo")
            return

        else:
            conta_logada["extrato"].append({
            "tipo": tipo,
            "data": datetime.now().strftime("%d/%m/%y"),
            "hora": datetime.now().strftime("%H/%M/%S"),
            "valor": - valor,
            "pessoa": destinatario["info_conta"]["nome"]
            })
            conta_logada["info_conta"]["saldo"] -= valor
            destinatario["info_conta"]["saldo"] += valor
            destinatario["extrato"].append({
            "tipo": tipo,
            "data": datetime.now().strftime("%d/%m/%y"),
            "hora": datetime.now().strftime("%H/%M/%S"),
            "valor": + valor,
            "pessoa": conta_logada["info_conta"]["nome"]
            })
            salvar_dados()
            return

def area_pix():
    while True:
        escolha = int(input("""
    ==== AREA PIX ====
    1 - cadastrar chave pix
    2 - lista de chave pix
    3 - remover chave pix
    4 - fazer pix
    5 - sair
     >>>"""))
        if escolha == 1: # cadastrar
            cadastrar_pix()

        elif escolha == 2:#lista de chaves
            lista_pix()

        elif escolha == 3:#remover chave pix
            remover_pix()

        elif escolha == 4: #fazer pix
            fazer_pix()

        elif escolha == 5:
            return
def cadastrar_pix():
    cadastro = input("digite a chave que você deseja salvar: ")
    if cadastro in conta_logada["chave_pix"]:
        print("esta chave ja existe")
    else:
        conta_logada["chave_pix"].append(cadastro)
        salvar_dados()
        return
def lista_pix():
    for item in conta_logada["chave_pix"]:
        print(item)
    return
def remover_pix():
    if conta_logada["chave_pix"] == None:
        print("não possui nenhuma chave cadastrada")
        return
    for indice, chave in enumerate(conta_logada["chave_pix"]):
        print(f"indice:{indice} chave: {chave}")
    escolha = int(input("digite qual o indice da cahve que deseja excluir: "))
    del conta_logada["chave_pix"][escolha]
    salvar_dados()
def fazer_pix():
    tipo = "pix"
    chave_desejada = input("digite a chave para qual deseja fazer o pix: ")
    for usuario in contas:
        if usuario["chave_pix"] in chave_desejada:
            conta_recebida = usuario
            break
    if not conta_recebida:
        print("usuario não existe!")
        return
    if conta_logada == conta_recebida:
        print("você não pode transferir para si mesmo!")
        return

    valor = int(input("quanto deseja transferir para essa pessoa?:"))
    if valor > conta_logada["info_conta"]["saldo"]:
        print("você não possui esse valor!")
        return

    conta_logada["info_conta"]["saldo"] -= valor
    conta_logada["extrato"].append({
    "tipo": tipo,
    "data": datetime.now().strftime("%d/%m/%y"),
    "hora": datetime.now().strftime("%H/%M/%S"),
    "valor": - valor,
    "pessoa": conta_recebida["info_conta"]["nome"],
    "chave": chave
    })

    conta_recebida["info_conta"]["saldo"] += valor
    conta_recebida["extrato"].append({
    "tipo": tipo,
    "data": datetime.now().strftime("%d/%m/%y"),
    "hora": datetime.now().strftime("%H/%M/%S"),
    "valor": + valor,
    "pessoa": conta_logada["info_conta"]["nome"],
    "chave": chave
    })
    salvar_dados()
    return
    
def procurar_conta_por_cpf(cpf): # verificar se cpf existe
    for usuario in contas:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def inicio(): # inicio 
    print("seja bem vindo a nossa agencia oque o senhor(a) deseja?")
    menu()
    return
inicio() # puxar inicio do programa