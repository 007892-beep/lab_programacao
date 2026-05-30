numeros = []
for i in range(6):
    num = int(input(f"Digite o número {i+1}: "))
    numeros.append(num)

x = int(input("Digite o número X para buscar: "))

contagem = numeros.count(x)
print(f"O número {x} aparece {contagem} vezes.")

if contagem > 0:
    indice = numeros.index(x)
    print(f"O índice da primeira ocorrência é: {indice}")
else:
    print("O número não está na lista.")
