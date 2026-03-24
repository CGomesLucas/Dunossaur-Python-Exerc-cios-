contador = 0
alturas = []
idades = []
media_alturas = 0
altura_abaixo_media = 0

while contador < 5:
 contador += 1
 print(f"Idade e altura do {contador}º aluno")
 idade = int(input("Insira a sua idade:"))
 altura = float(input("Insira a sua altura:"))
 idades += [idade]
 alturas += [altura]

media_alturas = sum(alturas) / len(alturas)

for x, y in zip(idades, alturas):
 if x > 13 and y < media_alturas:
    altura_abaixo_media += 1

print("A média de altura dos alunos é", media_alturas)
print("A quantidade de alunos que possui altura inferior a média de alturas é",
altura_abaixo_media)