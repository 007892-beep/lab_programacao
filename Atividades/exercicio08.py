vetor = [2.5, 7.5, 10.0, 4.0]

soma= 0
for numero in vetor:
    soma = soma + numero
    
media = soma / len(vetor)

valor_mais_proximo = vetor[0]

if vetor[0] > media:
    menor_diferenca = vetor[0] - media
else:
    menor_diferenca = media - vetor[0]
    
for numero in vetor:
    if numero > media:
        diferenca_atual = numero - media
 
    else:
        diferenca_atual = media - numero
        
    if diferenca_atual < menor_diferenca:
        menor_diferenca = diferenca_atual
        valor_mais_proximo = numero
        
print(f"media: {media}")
print(f"Valor mais proximo da media: {valor_mais_proximo}")    
        
