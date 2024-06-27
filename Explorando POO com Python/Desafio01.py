class UsuarioTelefone:
    PLANOS_VALIDOS = ["Plano Essencial Fibra", "Plano Prata Fibra", "Plano Premium Fibra"]
    
    def __init__(self, nome, numero, plano):
        self._nome = nome
        self._numero = numero
        self._plano = plano
        self._validar_plano()
    
    def _validar_plano(self):
        if self._plano not in self.PLANOS_VALIDOS:
            raise ValueError(f"Plano '{self._plano}' inválido. Os planos válidos são: {', '.join(self.PLANOS_VALIDOS)}")
    
    def __str__(self):
        return f"Usuário {self._nome} criado com sucesso."
    
nome = input()  
numero = input() 
plano = input()   

try:
    usuario = UsuarioTelefone(nome, numero, plano)
    
    print(usuario)
except ValueError as e:
    print(e)
