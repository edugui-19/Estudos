menu = """

[1] Depositar
[2] Sacar
[3] Extrato

[0] Sair

=> """

saldo = 0
limite = 500
extrato = []
saquesRestantes = 3

while True:

    opcao = input(menu)

    if opcao == "1":        ##OPERAÇÃO DE DEPÓSITO
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}\n")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":      ##OPERAÇÃO DE SAQUE
        valor = float(input("Informe o valor do saque: "))


        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif saquesRestantes == 0:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            saquesRestantes -= 1
            extrato.append(f"Saque: R$ {valor:.2f}\n")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":      ##OPERAÇÃO DE VISUALIZAÇÃO DO EXTRATO
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else "".join(extrato))
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        break

    else:
        print("Operação falhou! Por favor, selecione uma opção válida.")