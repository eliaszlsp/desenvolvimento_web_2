
def calcular_media():
    notas = []

    while len(notas) < 5:
        nota = float(input(f"Digite uma nota ({len(notas) + 1}/5): "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    print(f"A média das notas é: {media}")
