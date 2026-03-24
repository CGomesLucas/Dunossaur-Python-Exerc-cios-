contador = 0
idades = []
alturas = []

print("Ordem Lida")
while contador < 3:
    contador += 1
    print(f"Insira a idade e altura da {contador}º pessoa")
    idade = int(input("Insira a sua idade: "))
    altura = float(input("Insira a sua altura: "))

    idades += [idade]
    alturas += [altura]

print("Ordem lida\n")
print(idades)
print(alturas)
print("\nOrdem Inversa a Ordem Lida\n")
print(idades[::-1])
print(alturas[::-1])


