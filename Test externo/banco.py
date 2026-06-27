contas = [
{"cpf": 1020,
"limitesaque": 0,
"limitedeposito": 0,
"extrato": [],
"info_conta": {
"data_criação": "27/06/2026",
"ultimo_login": "",
"quantida_login": 0,
"nome":"kiko",
"senha": 10,
"saldo": 1000,
}},
{"cpf": 1030,
"limitesaque": 0,
"limitedeposito": 0,
"extrato": [],
"info_conta": {
"data_criação": "27/06/2026",
"ultimo_login": "",
"quantida_login": 0,
"nome":"mario",
"senha": 20,
"saldo": 3000,


}
}]

conta_logada = None
from datetime import datetime

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
        4 - encerrar programa
        ====================
        """)
            try:
                escolha = int(input(">>>"))
            except:
                print("insira valor valido")

            if escolha in (1,2,3,4,):
                break

        if escolha == 1: #criar conta
            criar_conta()

        elif escolha == 2: #entrar em uma conta
            entrar_conta()

        elif escolha == 3: #lista de contas
            lista_usuarios()

        elif escolha == 4:
            print("obrigado por entrar na nossa agencia, tenha um bom dia")
            exit()

def criar_conta(): # criando conta
    global contas
    while True:
            usuario_existe = False
            cpf = int(input("digite seu cpf:"))
            nome = input("digite seu nome:")

            while True: # verificar usuario igual
                while True:# verificação de senha igual

                    try:
                        senha = int(input("digite sua senha(somente numeros):"))
                    except:
                        print("erro de senha, deve ser somente numero")
                    try:
                        senhateste = int(input("digite sua senha novamente:"))
                    except:
                        print("senha deve ser somente numero")

                    if senha == senhateste:
                        for usuario in contas: 
                            if usuario["cpf"] == cpf:
                               usuario_existe = True

                        if usuario_existe == True:
                            print("ja existe um usuario com este cpf")

                        elif usuario_existe == False:
                            contas.append({"cpf": cpf ,"limitesaque": 0,
                            "limitedeposito": 0, "extrato": [],
                            "info_conta": {
                            "data_criação": datetime.now().strftime("%d/%m/%Y"),
                            "quantida_login": 0,
                            "nome":nome,"senha": senha,
                            "saldo": 0,
                            }})

                            print("conta criada com sucesso!")
                            break
                        break
                    else:
                        print("!as duas senha devem ser iguais!")
           
                break
            break
    return
def lista_usuarios():
    for usuario in contas:
        print(usuario["info_conta"]["nome"])

    return
def entrar_conta():
    global conta_logada
    while True:
        usuario_existe = False
        cpf = int(input("digite seu cpf:"))
        senha = int(input("digite sua senha:"))
        for usuario_logado in contas:
            if usuario_logado["cpf"] == cpf and usuario_logado["info_conta"]["senha"] == senha:
                usuario_existe = True
                break
               
        if usuario_existe == True:

            conta_logada = usuario_logado
            conta_logada["info_conta"]["quantida_login"] += 1
            conta_logada["info_conta"]["ultimo_login"] = datetime.now().strftime("%d/%m/%y")
            print(f"você logou em {usuario_logado}")
            break
        else:
            print("usuario inexistente, voltando ao menu...")
            return
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
                print(item)
            return
        elif escolha == 5: # ver informações da conta
            for item in conta_logada["info_conta"].items():
                print(item)
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
    return
def alterar_nome():
    while True:
        novo_nome1 = input("digite seu novo nome:")
        novo_nome2 = input("digite seu novo nome novamente:")

        if novo_nome2 != novo_nome1:
            print("os dois nomes devem ser iguais!")

        else:
            conta_logada["info_conta"]["nome"] = novo_nome1
            return
def alterar_senha():
    while True:
        nova_senha1 = int(input("digite sua nova senha:")) 
        nova_senha2 = int(input("digite sua nova senha novamente:")) 

        if nova_senha1 != nova_senha2:
            print("as duas senha devem ser iguais!")

        else:
            conta_logada["info_conta"]["senha"] = nova_senha1
            return

def menu_bancario():
    global conta_logada
    while True:
        escolha = int(input(f"""
        ==== MINHA CONTA ====
        nome: {conta_logada["info_conta"]["nome"]}
        saldo: {conta_logada["info_conta"]["saldo"]}
        senha: {conta_logada["info_conta"]["senha"] }
        numero de logins: {conta_logada["info_conta"]["quantida_login"]}
        === MENU BANCARIO ===
        1 - consultar saldo
        2 - depositar
        3 - sacar
        4 - transferir
        5 - opção de conta
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

        elif escolha == 5: # opção de conta
            opção_conta()

            return
def consultar_saldo():
    type = "consulta"

    print(f"seu saldo atual é : {conta_logada["info_conta"]["saldo"]}")

    conta_logada["extrato"].append({
    "tipo": type,
    "data": datetime.now().strftime("%d/%m/%y"),
    "hora": datetime.now().strftime("%H/%M/%S")
    
    })
    return
def depositar():
    type = "depositar"
    if conta_logada["limitedeposito"] > 3:
        print("você ja alcançou seu limite de depositos")
        return

    else:
        deposito = int(input("qual valor você deseja depositar?:"))

        if deposito < 0:
            print("você não pode depositar valor negativo")

        else:
            conta_logada["extrato"].append({   
    "tipo": type,
    "data": datetime.now().strftime("%d/%m/%y"),
    "hora": datetime.now().strftime("%H/%M/%S"),
    "valor": deposito
    })
            conta_logada["info_conta"]["saldo"] += deposito
            conta_logada["limitedeposito"] += 1
    return
def sacar():
    type = "saque"
    if conta_logada["limitesaque"] > 3:
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
    "tipo": type,
    "data": datetime.now().strftime("%d/%m/%y"),
    "hora": datetime.now().strftime("%H/%M/%S"),
    "valor": - saque
            })
            conta_logada["info_conta"]["saldo"] -= saque
            conta_logada["limitesaque"] += 1
    return
def transferir():
    type = "transferencia"
    global contas
    usuario_existe = False
    destinatario = int(input("digite o cpf de quem deseja transferir:"))
    for usuario_destinatario in contas:
        if usuario_destinatario["cpf"] == destinatario:
            usuario_existe = True

    if usuario_destinatario["cpf"] == conta_logada["cpf"]:
        print("você não pode transferir para si mesmo")

    if usuario_existe == True :
        destinatario = usuario_destinatario
        print("usuario existente")
        valor = int(input("quanto deseja transferir para esse pessoa?:"))

        if valor < 0:
            print("você não pode transferir valor negativo")

        elif valor > conta_logada["info_conta"]["saldo"]:
            print("você não possui saldo")
            return

        else:
            conta_logada["extrato"].append({
    "tipo": type,
    "data": datetime.now().strftime("%d/%m/%y"),
    "hora": datetime.now().strftime("%H/%M/%S"),
    "valor": - valor,
    "pessoa": destinatario["info_conta"]["nome"]
            })
            conta_logada["info_conta"]["saldo"] -= valor
            destinatario["info_conta"]["saldo"] += valor
            destinatario["extrato"].append({
    "tipo": type,
    "data": datetime.now().strftime("%d/%m/%y"),
    "hora": datetime.now().strftime("%H/%M/%S"),
    "valor": + valor,
    "pessoa": conta_logada["info_conta"]["nome"]

            })

        
    else:
        print("usuario inexistente")
        return

def inicio(): # inicio 
    print("seja bem vindo a nossa agencia oque o senhor(a) deseja?")
    menu()
    return
inicio() # puxar inicio do programa