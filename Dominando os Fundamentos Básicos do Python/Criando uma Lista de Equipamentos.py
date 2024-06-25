# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []

# TODO: Crie um loop para solicitar os itens ao usuário:
for i in range(3):
    # Solicita o item e armazena na variável "equipamento":
    equipamento = input()
    # Adiciona o item à lista "itens":
    itens.append(equipamento)

# Exibe a lista de itens
print("Lista de Equipamentos:")
for item in itens:
    # Imprime cada item da lista formatado com um prefixo '-'
    print(f"- {item}")
