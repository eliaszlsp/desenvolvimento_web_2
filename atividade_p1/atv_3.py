
from modules.numero_primo import primo
from modules.soma_recursiva import soma_lista
from modules.contar_palavras import contar_palavras
from modules.registro_info import registrar_info


print("Teste de número primo:")
numero = int(input("Digite um número para verificar se é primo: "))
print(f"{numero} é primo? {primo(numero)}")
print()


print("Teste de soma recursiva:")
entrada_lista = input(
    "Digite os números da lista separados por espaço (ex: 1 2 3 4 5): ")
lista = [int(numero) for numero in entrada_lista.split()]
print(f"Soma da lista {lista}: {soma_lista(lista)}")
print()


print("Teste de contagem de palavras:")
texto = input("Digite um texto para contar as palavras: ")
print(f"Número de palavras no texto: {contar_palavras(texto)}")
print()

print("Teste de registro de informações:")
print("Digite os argumentos posicionais (separados por espaço):")
args_input = input().split()

args = [int(arg) if arg.isdigit() else arg for arg in args_input]

print("\nDigite os argumentos nomeados (no formato chave=valor, separados por espaço):")
kwargs_input = input().split()
kwargs = {chave: int(valor) if valor.isdigit() else valor for chave, valor in (
    item.split("=") for item in kwargs_input)}

registrar_info(*args, **kwargs)
