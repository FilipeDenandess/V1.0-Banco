import textwrap
from datetime import datetime

usuarios = {}     
contas  = []           
contador_contas = 1000 
LIMITE_SAQUE_VALOR  = 500
LIMITE_SAQUE_QTD    = 3
AGENCIA             = "0001"

# ============== MENUS ==============

def menu_principal():
    print(textwrap.dedent("""
    ===== Menu Principal =====
    [1] Criar usuário
    [2] Login
    [3] Listar contas
    [0] Sair
    =========================="""))

def menu_logado(nome):
    print(textwrap.dedent(f"""
    ===== Banco - Usuário {nome} =====
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Logout
    ================================"""))


# ============== FUNÇÕES DE USUÁRIO/CONTA ==============

def criar_usuario():
    global contador_contas

    nome = input("→ Novo nome de usuário: ").strip()
    if nome in usuarios:
        print("Usuário já existe.\n")
        return

    senha = input("→ Defina uma senha: ").strip()

    contador_contas += 1
    conta_numero = contador_contas

    usuarios[nome] = {
        "senha"        : senha,
        "conta"        : {"agencia": AGENCIA, "numero": conta_numero},
        "saldo"        : 0.0,
        "extrato"      : [],
        "saques_dia"   : 0            
    }
    contas.append({"agencia": AGENCIA, "numero_conta": conta_numero, "titular": nome})
    print(f"✓ Conta criada! Agência {AGENCIA}  Conta {conta_numero}\n")

def listar_contas():
    if not contas:
        print("Nenhuma conta criada ainda.\n")
        return
    for c in contas:
        print("="*40)
        print(f"Agência: {c['agencia']}  |  Conta: {c['numero_conta']}  |  Titular: {c['titular']}")
    print("="*40 + "\n")

def autenticar():
    nome = input("Usuário: ").strip()
    senha = input("Senha  : ").strip()

    if nome in usuarios and senha == usuarios[nome]["senha"]:
        print(f"\nBem‑vindo, {nome}!\n")
        return nome
    print("✗ Credenciais inválidas.\n")
    return None



def depositar(u_data):
    try:
        valor = float(input("Valor do depósito: R$ "))
        if valor <= 0:
            raise ValueError
    except ValueError:
        print("✗ Valor inválido.\n")
        return

    u_data["saldo"] += valor
    u_data["extrato"].append(("Depósito", valor, datetime.now()))
    print("✓ Depósito realizado.\n")

def sacar(u_data):
    try:
        valor = float(input("Valor do saque: R$ "))
        if valor <= 0:
            raise ValueError
    except ValueError:
        print("✗ Valor inválido.\n")
        return

    if valor > u_data["saldo"]:
        print("✗ Saldo insuficiente.\n")
        return
    if valor > LIMITE_SAQUE_VALOR:
        print(f"✗ Limite por saque é R${LIMITE_SAQUE_VALOR:.2f}.\n")
        return
    if u_data["saques_dia"] >= LIMITE_SAQUE_QTD:
        print("✗ Limite de saques diários atingido.\n")
        return

    u_data["saldo"] -= valor
    u_data["saques_dia"] += 1
    u_data["extrato"].append(("Saque   ", -valor, datetime.now()))
    print("✓ Saque realizado.\n")

def exibir_extrato(u_data):
    print("\n======= EXTRATO =======")
    if not u_data["extrato"]:
        print("Sem movimentações.")
    else:
        for tipo, valor, data in u_data["extrato"]:
            print(f"{data.strftime('%d/%m %H:%M')} | {tipo}: R$ {valor:+.2f}")
    print(f"Saldo atual: R$ {u_data['saldo']:.2f}")
    print("=======================\n")



def main():
    while True:
        menu_principal()
        escolha = input("Escolha: ").strip()

        if escolha == "1":
            criar_usuario()

        elif escolha == "2":
            user = autenticar()
            if not user:
                continue


            while True:
                menu_logado(user)
                op = input("Opção: ").strip()

                if   op == "1":
                    depositar(usuarios[user])
                elif op == "2":
                    sacar(usuarios[user])
                elif op == "3":
                    exibir_extrato(usuarios[user])
                elif op == "4":
                    print("Logout efetuado.\n")
                    break
                else:
                    print("Opção inválida.\n")
          

        elif escolha == "3":
            listar_contas()

        elif escolha == "0":
            print("Obrigado por usar o Banco!")
            break
        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    main()
