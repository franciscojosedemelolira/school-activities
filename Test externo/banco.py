contas = [
{"nome":"kiko",
"senha": 10,
"saldo": 1000,
"extrato": {
    "valor_transferido": 0,
    "pessoa_transferencia": [],
    "valor_recebido": 0,
    "pessoa_recebido": [],
    "valor_sacado": 0 ,
    "valor_depositado": 0}},
{"nome":"mario",
"senha": 20,
"saldo": 3000,
"extrato": {
    "valor_transferido": 0,
    "pessoa_transferencia": [],
    "valor_recebido": 0,
    "pessoa_recebido": [],
    "valor_sacado": 0 ,
    "valor_depositado": 0}}]

conta_logada = None

def menu():
    while True:
        while True:
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
                            if usuario["nome"] == nome:
                               usuario_existe = True
                        if usuario_existe == True:
                            print("ja existe um usuario com este nome")
                        elif usuario_existe == False:
                            contas.append({"nome":nome,"senha": senha, "saldo": 0, "extrato": {"valor_transferido": 0, "pessoa_transferencia": [], "pessoa_recebido": [], "valor_recebido": 0, "valor_sacado": 0 , "valor_depositado": 0}})

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
        print(usuario["nome"])
    return
def entrar_conta():
    global conta_logada
    while True:
        usuario_existe = False
        nome = input("digite seu nome:")
        senha = int(input("digite sua senha:"))
        for usuario_logado in contas:
            if usuario_logado["nome"] == nome and usuario_logado["senha"] == senha:
                usuario_existe = True
                break
               
        if usuario_existe == True:

            conta_logada = usuario_logado
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
    2 - alterar senha
    3 - extrato 
    4 - sair 
    ======================
     >>>"""))
        if escolha == 1: #excluir conta
            escolha = int(input("""
            você reamente deseja excluir sua conta?
            1 - sim
            2 - não 
             >>>"""))
            if escolha == 1:
                print("você é louco!")
                contas.remove(conta_logada)
                return

        elif escolha == 2: #alterar senha
            while True:
                nova_senha1 = int(input("digite sua nova senha:")) 
                nova_senha2 = int(input("digite sua nova senha novamente:")) 
                if nova_senha1 != nova_senha2:
                    print("as duas senha devem ser iguais!")
                else:
                    conta_logada["senha"] = nova_senha1
                    return

        elif escolha == 3: # extrato
            for item in conta_logada["extrato"].items():
                print(item)
            return
            
        elif escolha == 4: # sair
            print("saindo da conta")
            conta_logada = None
        return

def menu_bancario():
    global conta_logada
    while True:
        escolha = int(input("""
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
    print(f"seu saldo atual é : {conta_logada["saldo"]}")
    return
def depositar():
    deposito = int(input("qual valor você deseja depositar?:"))
    if deposito < 0:
        print("você não pode depositar valor negativo")
    else:
        conta_logada["extrato"]["valor_depositado"] += deposito
        conta_logada["saldo"] += deposito
    return
def sacar():
    saque = int(input("digite o quanto quer sacar:"))

    if saque > conta_logada["saldo"]:
        print("você não possui esse valor em conta")

    elif saque < 0:
        print("você não pode sacar valor negativo")

    else:
        conta_logada["extrato"]["valor_sacado"] += saque
        conta_logada["saldo"] -= saque
    return
def transferir():
    global contas
    usuario_existe = False
    destinatario = input("digite para quem deseja transferir:")
    for usuario_destinatario in contas:
        if usuario_destinatario["nome"] == destinatario:
            usuario_existe = True

    if usuario_destinatario["nome"] == conta_logada["nome"]:
        print("você não pode transferir para si mesmo")

    if usuario_existe == True :
        destinatario = usuario_destinatario
        print("usuario existente")
        valor = int(input("quanto deseja transferir para esse pessoa?:"))
        if valor < 0:
            print("você não pode transferir valor negativo")
        elif valor > conta_logada["saldo"]:
            print("você não possui saldo")
            return

        else:
            conta_logada["extrato"]["pessoa_transferencia"].append(destinatario["nome"])
            conta_logada["extrato"]["valor_transferido"] += valor
            destinatario["extrato"]["pessoa_recebido"].append(conta_logada["nome"])
            destinatario["extrato"]["valor_recebido"] += valor 
            conta_logada["saldo"] -= valor
            destinatario["saldo"] += valor
        
    else:
        print("usuario inexistente")
        return

def inicio(): # inicio 
    print("seja bem vindo a nossa agencia oque o senhor(a) deseja?")
    menu()
    return
inicio() # puxar inicio do programa