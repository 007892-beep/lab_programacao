def aluno_nota(nota):
    if nota >= 6:
        return "Aprovado"
    elif 4 <= nota < 6:
        return "Verificação Suplementar"
    else:
        return "Reprovado"
    
nota_do_aluno=int(input("insira sua nota: "))

resultado = aluno_nota(nota_do_aluno)

print(f"A  sua nota é{nota_do_aluno} e seu resultado é {resultado}")
