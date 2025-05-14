saldo = 0
limite = 500
extrato = []
saquesRestantes = 3

## ---------- MENSAGEM DO MENU
menu = """

[1] Depositar
[2] Sacar
[3] Extrato

[0] Sair

=> """

## ---------- FUNÇÃO PARA VALIDAÇÃO E EXECUÇÃO DO SAQUE
def realizar_saque(valor, saldo, limite, saquesRestantes, extrato):
    ##--FALHAS
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif saquesRestantes == 0:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor <= 0:
        print("Operação falhou! O valor informado é inválido.")

    ##--SAQUE APROVADO
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}\n")
        saquesRestantes -= 1
        print("Saque realizado com sucesso!")

    return saldo, extrato, saquesRestantes

## ---------- TERMINAL
while True:
    opcao = input(menu)

    if opcao == "1":        ##OPERAÇÃO DE DEPÓSITO
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}\n")
            print("Depósito realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":      ##OPERAÇÃO DE SAQUE
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, saquesRestantes = realizar_saque(valor, saldo, limite, saquesRestantes, extrato)

    elif opcao == "3":      ##OPERAÇÃO DE VISUALIZAÇÃO DO EXTRATO
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print("".join(extrato))
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")


    elif opcao == "0":      ##OPERAÇÃO PARA SAIR DO SISTEMA
        break

    else:
        print("Operação falhou! Por favor, selecione uma opção válida.")