
listaRoupas = ["calça", "sapato", "camisa"]

precoRoupas = ["100", "150", "80"]

carrinho = []
for i in range(len(listaRoupas)):
    produtos = f"numero :{i} roupa:{listaRoupas[i]}  preço = {precoRoupas[i]}"
    print(produtos)
while True:
    numeroEscolhido = int(input("escolha seu produto "))
    carrinho.append(listaRoupas[numeroEscolhido])
    comprarMais = input("quer comprar mais? S/N").lower()
    if comprarMais == "n":
        break

print(f"produtos comprados  = {",".join(carrinho)}")
