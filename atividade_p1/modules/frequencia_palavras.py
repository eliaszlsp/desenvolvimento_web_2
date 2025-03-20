from .contar_palavras import contar_palavras


def contar_frequencia(texto):
    frequencia_palavra = texto.lower()
    frequencia_palavra = texto.split()
    contagem = {}

    print("Frequência das palavras no texto:")
    for palavra in frequencia_palavra:
        contagem[palavra] = len(contagem) + 1

    for palavra, frequencia in contagem.items():

        print(f"{palavra}: {frequencia}")

    print(f"Total de palavras no texto: {contar_palavras(texto)}")
