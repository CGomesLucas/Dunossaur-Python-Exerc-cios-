contador = 0
medias = []
media_maior_igual_7 = []

while contador < 5:
    contador += 1
    print(f"Insira as 4 notas do {contador}º aluno")
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    nota4 = float(input('Digite a quarta nota: '))

    media = (nota1 + nota2 + nota3 + nota4) / 4
    medias += [media]

for i in medias:
    if i >= 7:
        media_maior_igual_7 += [i]

print(f"O número de alunos com média maior ou igual a 7 é {len(media_maior_igual_7)}")








