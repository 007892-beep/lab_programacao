nomes = []
for i in range(5):
    nome = input(f"Digite o nome {i+1}: ")
    nomes.append(nome)
nomes_inversos = nomes[::-1]

print("Lista original:", nomes)
print("Lista invertida:", nomes_inversos)
