letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
qtd_consoantes = 0
letras_consoantes = []

for letra in letras:
    if letra != 'A' and letra != 'E' and letra != 'I' and letra != 'O' and letra != 'U':
        letras_consoantes += letra

print(letras_consoantes) # não imprime a, e, i
print(f"Foram lidas {len(letras_consoantes)} consoantes")


