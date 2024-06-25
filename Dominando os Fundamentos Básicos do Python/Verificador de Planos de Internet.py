def recomendar_plano(consumo):
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo > 10 and consumo <= 20:
        return "Plano Prata Fibra - 100Mbps"
    elif consumo > 20:
        return "Plano Premium Fibra - 300Mbps"
    else:
        return "Consumo inválido."

consumo = float(input())
plano_recomendado = recomendar_plano(consumo)
print(plano_recomendado)
