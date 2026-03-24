numeros = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
numeros_quadrado = []

for numero in numeros:
 numeros_quadrado += [numero ** 2]

print(numeros_quadrado)
print("A soma dos quadrados dos elementos do vetor é igual a:", sum(numeros_quadrado))