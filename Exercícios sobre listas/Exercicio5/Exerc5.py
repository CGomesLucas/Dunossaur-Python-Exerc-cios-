numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numeros_pares = []
numeros_impares = []

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares += [numero]
    else:
        numeros_impares += [numero]

print(numeros_pares)
print(numeros_impares)
