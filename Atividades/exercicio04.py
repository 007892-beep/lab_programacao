lista1 = [1,2,3,4]
lista2 = [10,20,30,40,50,60]
lista_intercalada = [1, 10, 2, 20, 3, 30, 4, 40, 50, 60]

if len(lista1) < len(lista2):
    menor = lista1
    maior = lista2
else:
    menor = lista2
    maior = lista1

lista_intercalada = []

for i in range(len(menor)):
    lista_intercalada.append(menor[i])
    lista_intercalada.append(maior[i])

    lista_intercalada.extend(maior[len(menor):])

print("Resultado:", lista_intercalada)