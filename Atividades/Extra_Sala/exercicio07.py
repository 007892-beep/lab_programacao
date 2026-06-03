#Separador de par/impar Dinamico
#elaborar um programa que leia 10 numeros interiso do teclado
# a medida q os numeros forem lidos os pares devem ser inseridos em uma lista chamada pares e os impares em uma lista chamada impares

pares = []
impares = []

while len(pares) + len(impares) < 10: #enquanto eu n tiver 10 numeros guardados,continue perguntando
    num = int(input(f"Digite o {len(pares)}"))

    #verifica se o numero ja existai em qualquer umas das listas
    if num in pares or num in impares:
        print("Número já inserido anteriormente. Por favor, digite outro.") 
    else:
        if num % 2 == 0: #O código verifica a condição (num % 2 == 0). Se for verdadeira, o destino é a lista pares.
            pares.append(num)
        else: 
            impares.append(num)

print("Entrada inválida. Digite apenas númneros inteiros.")
print("\nLista de pares:", pares)
print("Lista de ímpares:", impares)
