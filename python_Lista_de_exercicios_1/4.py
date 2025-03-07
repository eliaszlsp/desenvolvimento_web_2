
carteira = 1000

listaRoupas = ["calça", "sapato", "camisa"]

precoRoupas = [100, 150, 800]

carrinho = []
valorTotal = 0
for i in range(len(listaRoupas)):
    produtos = f"numero :{i} roupa:{listaRoupas[i]}  preço = {precoRoupas[i]}"
    print(produtos)


while True:
    numeroEscolhido = int(input("escolha seu produto "))
    if carteira < precoRoupas[numeroEscolhido]:
        print("Saldo insuficiente!!!! escolha outro produto ou finalize a compra")
        comprarMais = input("quer comprar mais? S/N").lower()
        if comprarMais == "n":
            break
    else:
        carrinho.append(listaRoupas[numeroEscolhido])
        valorTotal += precoRoupas[numeroEscolhido]
        carteira -= precoRoupas[numeroEscolhido]
        comprarMais = input("quer comprar mais? S/N").lower()
        if comprarMais == "n":
            break

print(
    f"produtos comprados  = {",".join(carrinho)} valor total : {valorTotal}  troco/saldo : {carteira}")
