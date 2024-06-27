# Classe UsuarioTelefone com encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self._nome = nome
        self._numero = numero
        self._plano = plano

    def fazer_chamada(self, destinatario, duracao):
        custo = self._plano.custo_chamada(duracao)
        saldo_atual = self._plano.verificar_saldo()
        
        if saldo_atual >= custo:
            self._plano.deduzir_saldo(custo)
            saldo_restante = self._plano.verificar_saldo()
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${saldo_restante:.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."

class Plano:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial

    def verificar_saldo(self):
        return self._saldo

    def custo_chamada(self, duracao):
        return 0.10 * duracao

    def deduzir_saldo(self, valor):
        self._saldo -= valor

class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


nome = input()
numero = input()
saldo_inicial = float(input())


usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)

destinatario = input()
duracao = int(input())

print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
