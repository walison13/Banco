
saldo = 0
calculo = 0
acumulador_de_extrato = ''

while True:

    print("*" * 50)
    print("{:^50}".format('Banco Dinheiro Feliz'))
    print("*" * 50)
    print("""
                    [1]Saque
                    [2]Depósito
                    [3]Extrato
                    [4]Sair 
    """)

    opcao = input("Digite sua opção: ")

    def Saque(saque, limite=500):
        global saldo, calculo, acumulador_de_extrato

        if saque > limite:
            return f"Saque inválido, seu limite é de R${limite:.2f}"

        elif saldo == 0 or saque < 0:
            return f"Saque inválido, seu saldo é de R$:{saldo:.2f}"

        elif saque > saldo:
            return f"Saque de R$:{saque:.2f} negado, seu saldo é de R$:{saldo:.2f}"

        elif calculo > 3:
            return f"Saque negado, seu limite foi excedido"

        calculo += 1
        acumulador_de_extrato += f"Saque R$:{saque:.2f}\n"
        saldo -= saque

        return f"Saque de R$:{saque:.2f} feito com sucesso"

    def Deposito(deposito):
        global saldo
        if deposito < 0:
            return f"Deposito inválido"

        saldo += deposito
        return "Deposito feito com sucesso"

    def Extrato():
        print("#" * 15, "Extrato Bancário", "#" * 15)
        print(f"Saldo R$:{saldo:.2f}")
        print(f"\n{acumulador_de_extrato}")

    if opcao == '1':
        saque = float(input("Quanto você quer sacar R$: "))
        sacar = Saque(saque)
        print(sacar)

    elif opcao == '2':
        deposito = float(input("Quanto você quer depositar R$: "))
        deposito = Deposito(deposito)
        print(deposito)

    elif opcao == '3':
        Extrato()

    elif opcao == '4':
        print("Você saiu, obrigado, volte sempre!")
        break

    else:
        print("Comando inválido, tente de novo")
