notas =[]
for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)
menor_nota = min(notas)
notas.remove(menor_nota)

print(f"\nA menor nota ({menor_nota}) foi removida.")
print(f"Notas restantes na lista: {notas}")
