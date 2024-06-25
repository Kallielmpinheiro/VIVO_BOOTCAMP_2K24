from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    def __str__(self):
        return f"Cliente: {self.__nome}, CPF: {self.__cpf}"

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento):
        super().__init__(nome, cpf)
        self.__data_nascimento = data_nascimento

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    def __str__(self):
        return f"{super().__str__()}, Data de Nascimento: {self.__data_nascimento}"

class Transacao(ABC):
    @abstractmethod
    def depositar(self, valor: float):
        pass

    @abstractmethod
    def sacar(self, valor: float):
        pass

class ContaBancaria(Transacao):
    def __init__(self, numero_conta, cliente):
        self.__numero_conta = numero_conta
        self.__saldo = 0.0
        self.__cliente = cliente

    @property
    def numero_conta(self):
        return self.__numero_conta

    @property
    def saldo(self):
        return self.__saldo

    @property
    def cliente(self):
        return self.__cliente

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado. Saldo atual: {self.__saldo}")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado. Saldo atual: {self.__saldo}")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def __str__(self):
        return f"Conta: {self.__numero_conta}, Saldo: {self.__saldo}, {self.__cliente}"

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, cliente, limite):
        super().__init__(numero_conta, cliente)
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite

    def sacar(self, valor):
        if 0 < valor <= (self.saldo + self.__limite):
            self._ContaBancaria__saldo -= valor  # Acessando saldo privado da superclasse
            print(f"Saque de {valor} realizado com cheque especial. Saldo atual: {self.saldo}")
        else:
            print("Saldo insuficiente, mesmo com cheque especial.")

    def __str__(self):
        return f"Conta Corrente: {self.numero_conta}, Saldo: {self.saldo}, Limite: {self.__limite}, {self.cliente}"

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_conta, cliente):
        super().__init__(numero_conta, cliente)

    def __str__(self):
        return f"Conta Poupança: {self.numero_conta}, Saldo: {self.saldo}, {self.cliente}"

def main():
    print("Cadastro do Cliente:")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    data_nascimento = input("Data de Nascimento: ")

    cliente = PessoaFisica(nome, cpf, data_nascimento)

    print("\nCadastro da Conta Corrente:")
    numero_conta_corrente = input("Número da Conta Corrente: ")
    limite = float(input("Limite do Cheque Especial: "))

    conta_corrente = ContaCorrente(numero_conta_corrente, cliente, limite)

    print("\nCadastro da Conta Poupança:")
    numero_conta_poupanca = input("Número da Conta Poupança: ")

    conta_poupanca = ContaPoupanca(numero_conta_poupanca, cliente)

    print("\nInformações da Conta Corrente:")
    print(conta_corrente)

    print("\nInformações da Conta Poupança:")
    print(conta_poupanca)

    while True:
        print("\nOperações:")
        print("1. Depósito na Conta Corrente")
        print("2. Saque na Conta Corrente")
        print("3. Depósito na Conta Poupança")
        print("4. Saque na Conta Poupança")
        print("5. Sair")
        opcao = input("Escolha uma operação: ")

        if opcao == '1':
            valor = float(input("Valor do depósito: "))
            conta_corrente.depositar(valor)
        elif opcao == '2':
            valor = float(input("Valor do saque: "))
            conta_corrente.sacar(valor)
        elif opcao == '3':
            valor = float(input("Valor do depósito: "))
            conta_poupanca.depositar(valor)
        elif opcao == '4':
            valor = float(input("Valor do saque: "))
            conta_poupanca.sacar(valor)
        elif opcao == '5':
            print("Encerrando operações.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
