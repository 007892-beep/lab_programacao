vetor = [2.5, 7.5, 10.0, 4.0]

media = sum(vetor) / len(vetor)

vetor_mais_proximo = vetor[0]
menor_difetrentes = abs(vetor[0] - media)

for numero in vetor:
    diferenca_atual = abs(numero - media)
    
    if diferenca_atual < abs(numero - media):
    
        menor_diferenca = diferenca_atual
        valor_mais_proximo = numero
    
print("vetor:", vetor)
print(f"Media: {media:.1f}")
print("valor mais proximo da media:", valor_mais_proximo)
