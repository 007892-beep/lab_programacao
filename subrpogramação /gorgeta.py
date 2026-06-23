ef calcular_gorjeta(valor, percentual=10):
    return valor * percentual/100


gorjeta = calcular_gorjeta(400)
print(f"O valor da gorjeta de 10% de uma conta de R$400 é: {gorjeta} ")
gorjeta = calcular_gorjeta(400, 5)
print("O valor da gorjeta de 5% de uma contta de R$400,00 é ", gorjeta)
