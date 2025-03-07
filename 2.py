frase = input("digite a frase\n")


separar = frase.split(" ")

print(separar)

contador = 0

for i in separar:
    for a in i:
        minusculo = a.lower()
        if minusculo == "a":
            contador += 1

frase = f"numero de letras 'a' na frase =  {contador}"
print(str(frase))
