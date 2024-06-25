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

while True:
    print(menu)
    opcao = input().strip().lower() 

    if opcao == 'q':
        print("Saindo...")
        break
    elif opcao == 'd':
        print("Informe o valor do depósito:")
        valorD = float(input())
        saldo += valorD  

    elif opcao == 's':
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diários alcançado.")
        else:
            print("Informe o valor que deseja sacar:")
            valorS = float(input()) 
            if valorS > saldo:
                print("Saldo insuficiente.")
            else:
                saldo -= valorS 
                numero_saques += 1

    elif opcao == 'e':
        print(f"Saldo atual: R$ {saldo:.2f}")
        print(f"Número de saques realizados hoje: {numero_saques}")

    else:
        print("Opção inválida. Tente novamente.")

print("Fim do programa.")
