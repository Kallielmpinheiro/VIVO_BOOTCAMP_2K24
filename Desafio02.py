menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 100
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 10

def deposito(saldo):
    valorD = float(input("Informe o valor do depósito: "))
    saldo += valorD
    return saldo

def saque(saldo, numero_saques):
    if numero_saques >= LIMITE_SAQUES:
        print("Limite de saques diários alcançado.")
    else:
        valorS = float(input("Informe o valor que deseja sacar: "))
        if valorS > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valorS
            numero_saques += 1
    return saldo, numero_saques

def extrato(saldo, numero_saques):
    print(f"Saldo atual: R$ {saldo:.2f}")
    print(f"Número de saques realizados hoje: {numero_saques}")

def main():
    while True:
        print(menu)
        opcao = input("Escolha uma opção: ").strip().lower()

        if opcao == 'q':
            print("Saindo...")
            break
        elif opcao == 'd':
            saldo = deposito(saldo)
        elif opcao == 's':
            saldo, numero_saques = saque(saldo, numero_saques)
        elif opcao == 'e':
            extrato(saldo, numero_saques)
        else:
            print("Opção inválida. Tente novamente.")

    print("Fim do programa.")

if __name__ == "__main__":
    main()
