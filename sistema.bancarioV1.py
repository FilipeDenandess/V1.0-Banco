saldo = 500
limite_saque = 500
EXTRATO = 3
extrato = int()

menu = f"""
========  Menu  =======

    Limite de saque: R${limite_saque}

    [D] Depositar
    [S] Sacar
    [E] Extrato

    [0] Sair

======================
Bem vindo! Escolha uma opção: 
"""

while True:
    opcao = input(menu)

    if opcao == "D":
        print("Deposito:")
        deposito = int(input("Quanto deseja depositar? R$:"))
        saldo = saldo + deposito
        extrato += deposito

        if deposito < 1:
            print("Erro ao depositar.")
        else:
            print(f"Deposito de R$:{deposito} concluido, acompanhe o valor em seu extrato.")


        
    elif opcao == "S":
        print("Saque:")
        saque = int(input(f"Quanto deseja sacar? Seu limite é R${limite_saque}. "))
        if saque < 1:
            print("Operação não realizada, valor inválido.")
        elif saque <= limite_saque & saque <= saldo:
            print(f"Saque de R${saque} realizado.")
            saldo = saldo - saque
            extrato += saque

        elif saque > saldo:
            print("Saldo insuficiente!")

        elif saque < 1:
            print("Operação não realizada, valor inválido.")

        else:
            print("Respeite seu limite de saque diário.")



    elif opcao == "E":
        print("Extrato:")
        if not extrato:
            print("Não há movimentações.")
        else:
            print(f"""
Saldo: R$:{saldo}
Ultimos Saques: R$:{saque}
Ultimos Depositos: R$:{deposito}
""")
    
    
    else:
        print("obrigado por utilizar o sistema!")
        break
