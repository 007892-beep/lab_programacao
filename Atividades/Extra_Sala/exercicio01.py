while True:
    num = int(input("Digite um numero (0 - para sair): "))
    if num == 0:
        print("Encerramento...")
        break
    if num >=10 and num <=50:
        print("Dado válido!")
    else:
        print("Dado inválido!")
