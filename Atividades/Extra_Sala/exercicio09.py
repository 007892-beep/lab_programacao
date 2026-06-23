historico = []

print("--- Simulador de Fluxo de Caixa ---")
print("Digite valores positivos para Receita e negativos para Despesa.")
print("Digite 0 para encerrar.\n")

while True:
    valor = float(input("Digite o valor da operação: R$ "))
    
    if valor == 0:
        break
        
    historico.append(valor)

for valor in historico[:]:
    if abs(valor) < 5.0:
        historico.remove(valor)

saldo_final = sum(historico)

print("\n----------------------------------")
print(f"Histórico após a limpeza: {historico}")
print(f"Saldo final remanescente: R$ {saldo_final:.2f}")
print("----------------------------------")

